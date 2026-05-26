from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


DATA_DIR = Path(r"C:\Users\e11338\Desktop\Feed System GAI\data")
INPUT_FILE = DATA_DIR / "FANUC_Specs.xlsx"
OUTPUT_FILE = DATA_DIR / "FANUC_Motor_Specs_Direct.xlsx"

ITEM_RENAMES = {
    "Rated Speed": "Rated rotation speed",
}

HEADER_MAP = {
    ("Continuous torque (at low speed) (*)", "Tc", "Nm"): "Continuous_Torque_Nm",
    ("Continuous torque (at low speed) (*)", "Tc", "kgfcm"): "Continuous_Torque_kgfcm",
    ("Continuous current (at low speed) (*)", "Ic", "A (rms)"): "Continuous_Current_A_rms",
    ("Rated output (*)", "Pr", "kW"): "Rated_Output_kW",
    ("Rated output (*)", "Pr", "HP"): "Rated_Output_HP",
    ("Rated rotation speed", "Nr", "min-1"): "Rated_Speed_RPM",
    ("Maximum rotation speed", "Nmax", "min-1"): "Maximum_Speed_RPM",
    ("Maximum torque (*)", "Tmax", "Nm"): "Maximum_Torque_Nm",
    ("Maximum torque (*)", "Tmax", "kgfcm"): "Maximum_Torque_kgfcm",
    ("Moment of inertia of rotor", "Jm", "kgm2"): "Rotor_Inertia_kgm2",
    ("Moment of inertia of rotor", "Jm", "kgfcms2"): "Rotor_Inertia_kgfcms2",
    ("Moment of inertia of rotor (with brake)", "Jm", "kgm2"): "Rotor_Inertia_Brake_kgm2",
    ("Moment of inertia of rotor (with brake)", "Jm", "kgfcms2"): "Rotor_Inertia_Brake_kgfcms2",
    ("Moment of inertia of rotor (with 35Nm brake)", "Jm", "kgm2"): "Rotor_Inertia_35Nm_Brake_kgm2",
    ("Moment of inertia of rotor (with 35Nm brake)", "Jm", "kgfcms2"): "Rotor_Inertia_35Nm_Brake_kgfcms2",
    ("Moment of inertia of rotor (with 70Nm brake)", "Jm", "kgm2"): "Rotor_Inertia_70Nm_Brake_kgm2",
    ("Moment of inertia of rotor (with 70Nm brake)", "Jm", "kgfcms2"): "Rotor_Inertia_70Nm_Brake_kgfcms2",
    ("Torque constant (*)", "Kt", "Nm/A (rms)"): "Torque_Constant_Nm_per_A_rms",
    ("Torque constant (*)", "Kt", "kgfcm/A (rms)"): "Torque_Constant_kgfcm_per_A_rms",
    ("Winding resistance (between terminals) (*)", "Ra", "Ohm"): "Winding_Resistance_Ohm",
    ("Thermal time constant", "tt", "min"): "Thermal_Time_Constant_min",
    ("Static friction", "Tf", "Nm"): "Static_Friction_Nm",
    ("Static friction", "Tf", "kgfcm"): "Static_Friction_kgfcm",
    ("Weight", "w", "kg"): "Weight_kg",
    ("Weight (with brake)", "w", "kg"): "Weight_Brake_kg",
    ("Weight (with 35Nm brake)", "w", "kg"): "Weight_35Nm_Brake_kg",
    ("Weight (with 70Nm brake)", "w", "kg"): "Weight_70Nm_Brake_kg",
    ("Max. current of servo amp.", "Imax", "A (peak)"): "Max_Servo_Amp_Current_A_peak",
}

KEY_ORDER = list(HEADER_MAP)


def clean_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def clean_unit(value) -> str:
    unit = clean_text(value)
    if unit == "\u03a9":
        return "Ohm"
    return unit


def clean_item(value) -> str:
    item = clean_text(value)
    return ITEM_RENAMES.get(item, item)


def parse_model(model: str) -> dict[str, object]:
    text = clean_text(model)
    match = re.match(
        r"^(?P<series>\u03b1i[SF])\s+"
        r"(?P<torque_class>\d+(?:\.\d+)?)/"
        r"(?P<speed>\d+)"
        r"(?P<option>.*?)"
        r"-D$",
        text,
    )
    if not match:
        return {
            "Series": "",
            "Torque_Class": "",
            "Nameplate_RPM": "",
            "Variant": "",
            "HV": False,
            "FAN": False,
        }

    option = re.sub(r"\s+", " ", match.group("option").strip())
    return {
        "Series": match.group("series"),
        "Torque_Class": float(match.group("torque_class")),
        "Nameplate_RPM": int(match.group("speed")),
        "Variant": option or "Standard",
        "HV": "HV" in option,
        "FAN": "FAN" in option,
    }


def output_column(row: pd.Series) -> str:
    key = (row["Item"], row["Symbol"], row["Unit"])
    base = HEADER_MAP.get(key)
    if base is None:
        safe_item = re.sub(r"[^A-Za-z0-9]+", "_", row["Item"]).strip("_")
        safe_symbol = re.sub(r"[^A-Za-z0-9]+", "_", row["Symbol"]).strip("_")
        safe_unit = re.sub(r"[^A-Za-z0-9]+", "_", row["Unit"]).strip("_")
        base = "_".join(part for part in [safe_item, safe_symbol, safe_unit] if part)
    return base if row["Split_Index"] == 1 else f"{base}_{row['Split_Index']}"


def ordered_columns(df: pd.DataFrame) -> list[str]:
    columns = []
    for key in KEY_ORDER:
        base = HEADER_MAP[key]
        matching = [col for col in df.columns if col == base or re.match(rf"^{re.escape(base)}_\d+$", col)]
        columns.extend(sorted(matching, key=lambda x: int(x.rsplit("_", 1)[1]) if x.rsplit("_", 1)[-1].isdigit() else 1))
    extras = [col for col in df.columns if col not in columns]
    return columns + sorted(extras)


def main() -> None:
    all_df = pd.read_excel(INPUT_FILE, sheet_name="ALL", engine="openpyxl")
    all_df = all_df.dropna(subset=["Model"]).copy()
    all_df["Model"] = all_df["Model"].map(clean_text)
    all_df["Item"] = all_df["Item"].map(clean_item)
    all_df["Symbol"] = all_df["Symbol"].map(clean_text)
    all_df["Unit"] = all_df["Unit"].map(clean_unit)

    meta = all_df["Model"].drop_duplicates().map(parse_model).apply(pd.Series)
    model_meta = pd.concat([all_df["Model"].drop_duplicates().reset_index(drop=True), meta.reset_index(drop=True)], axis=1)

    all_df["Split_Index"] = all_df.groupby(["Model", "Item", "Symbol", "Unit"]).cumcount() + 1
    all_df["Output_Column"] = all_df.apply(output_column, axis=1)

    model_by_item = all_df.pivot(index="Model", columns="Output_Column", values="Value").reset_index()
    model_by_item = model_meta.merge(model_by_item, on="Model", how="left")
    first_cols = ["Model", "Series", "Torque_Class", "Nameplate_RPM", "Variant", "HV", "FAN"]
    value_cols = ordered_columns(model_by_item.drop(columns=first_cols, errors="ignore"))
    model_by_item = model_by_item[first_cols + value_cols]

    item_index = (
        all_df.groupby(["Item", "Symbol", "Unit", "Output_Column"], dropna=False)
        .agg(Models_With_Value=("Model", "nunique"), Source_Rows=("Model", "size"))
        .reset_index()
    )

    duplicate_review = (
        all_df.groupby(["Model", "Item", "Symbol", "Unit"], dropna=False)
        .agg(
            Source_Values=("Value", lambda s: " | ".join(map(str, s.tolist()))),
            Unique_Values=("Value", lambda s: " | ".join(map(str, pd.unique(s).tolist()))),
            Source_Rows=("Value", "size"),
            Unique_Count=("Value", lambda s: len(pd.unique(s))),
        )
        .reset_index()
    )
    duplicate_review = duplicate_review[duplicate_review["Source_Rows"] > 1].copy()
    duplicate_review["Needs_Review"] = duplicate_review["Unique_Count"] > 1

    clean_cols = ["Model", "Series", "Torque_Class", "Nameplate_RPM", "Variant", "HV", "FAN"]
    all_clean = all_df.merge(model_meta, on="Model", how="left")
    all_clean = all_clean[clean_cols + ["Item", "Symbol", "Value", "Unit", "Split_Index", "Output_Column"]]

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        model_by_item.to_excel(writer, index=False, sheet_name="Model_By_Item")
        all_clean.to_excel(writer, index=False, sheet_name="ALL_Clean")
        item_index.to_excel(writer, index=False, sheet_name="Item_Index")
        duplicate_review.to_excel(writer, index=False, sheet_name="Duplicate_Review")

    print(f"Saved: {OUTPUT_FILE}")
    print(f"Source rows: {len(all_df)}")
    print(f"Model rows: {len(model_by_item)}")
    print(f"Unique models: {model_by_item['Model'].nunique()}")


if __name__ == "__main__":
    main()
