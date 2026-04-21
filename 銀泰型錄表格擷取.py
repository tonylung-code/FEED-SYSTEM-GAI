"""
PMI Catalog Table Extraction - Optimized for 6 key fields
Extract: 型號|外徑|導程|動負荷|靜負荷|剛性
"""

import pdfplumber
import pandas as pd
import re
from pathlib import Path


def extract_series_name(text):
    """Extract series name like FSIC, FDIC"""
    if not text:
        return "Unknown"
    match = re.search(r'(F[A-Z]{2,3}|R[A-Z]{2,3})', text)
    return match.group(1) if match else "Unknown"


def merge_multi_line_header(df, start_row=0, end_row=2):
    """Merge multi-line headers into single header row"""
    if end_row >= len(df):
        end_row = len(df) - 1
    
    new_columns = []
    for col_idx in range(df.shape[1]):
        col_parts = []
        for row_idx in range(start_row, end_row + 1):
            val = df.iloc[row_idx, col_idx]
            if val and str(val).strip() and str(val) != 'nan':
                col_parts.append(str(val).strip())
        
        col_name = ' '.join(col_parts) if col_parts else f'col_{col_idx}'
        new_columns.append(col_name)
    
    return new_columns


def find_data_start_row(df, max_header_rows=3):
    """Find where actual data starts (after multi-line header)"""
    for idx in range(max_header_rows, len(df)):
        row = df.iloc[idx]
        numeric_count = sum(pd.to_numeric(row, errors='coerce').notna())
        if numeric_count >= 3:  # At least 3 numeric values indicate data
            return idx
    return max_header_rows


def map_columns_to_required(raw_columns):
    """Map raw PDF columns to 6 required fields"""
    patterns = {
        '型號': r'型號|型号|model|MODEL|TYPE\b',
        '外徑': r'外徑|外径|Dg6\b|D6\b|diameter|螺帽.*Dg6',
        '導程': r'導程|导程|Lead\b|lead\b|pitch\b',
        '動負荷': r'動負荷.*Ca|Ca.*動負荷|Ca\b.*動|動.*Ca\b|基本額定負荷.*動負荷',
        '靜負荷': r'靜負荷.*Co|Co.*靜負荷|靜負荷\b|Co\b.*靜|靜.*Co\b',
        '剛性': r'剛性|刚性|Rigidity|rigidity|kfg.*rig',
    }
    
    mapping = {}
    for col_idx, raw_col in enumerate(raw_columns):
        if not raw_col or raw_col == 'nan' or pd.isna(raw_col):
            continue
        
        raw_col_str = str(raw_col).strip()
        # Skip generic column names
        if raw_col_str.startswith('col_'):
            continue
            
        for required_field, pattern in patterns.items():
            if required_field not in mapping:
                if re.search(pattern, raw_col_str, re.IGNORECASE):
                    mapping[required_field] = col_idx
                    break
    
    return mapping


def process_pdf_table(table, series_name, page_num):
    """Process a single table from PDF"""
    df = pd.DataFrame(table)
    df = df.dropna(how='all').dropna(axis=1, how='all')
    
    if df.shape[0] < 3 or df.shape[1] < 3:
        return None
    
    # Merge multi-line header
    new_columns = merge_multi_line_header(df, start_row=0, end_row=1)
    df.columns = new_columns
    print(f"  Table columns after merge: {new_columns}")
    
    # Find data start row
    data_start = find_data_start_row(df)
    if data_start >= len(df):
        print(f"  No valid data start row found")
        return None
    
    # Get column mapping
    col_mapping = map_columns_to_required(new_columns)
    print(f"  Column mapping: {col_mapping}")
    if not col_mapping:
        print(f"  No column mapping found")
        return None
    
    # Extract data
    output_data = []
    for idx in range(data_start, len(df)):
        row = df.iloc[idx]
        row_dict = {
            'Series_Name': series_name,
            'Source_Page': page_num + 1,
            '型號': None,
            '外徑': None,
            '導程': None,
            '動負荷': None,
            '靜負荷': None,
            '剛性': None,
        }
        
        for field, col_idx in col_mapping.items():
            value = row.iloc[col_idx] if col_idx < len(row) else None
            if value and str(value).strip():
                row_dict[field] = value
        
        # Debug: print first few rows
        if len(output_data) < 3:
            print(f"  Row {idx} data: {row_dict}")
        
        # Always add the row, don't filter by model
        output_data.append(row_dict)
    
    if not output_data:
        return None
    
    output_df = pd.DataFrame(output_data)
    
    # Generate model numbers before numeric conversion
    def generate_model_number(row):
        model_val = row.get('型號')
        if model_val and str(model_val).strip() and str(model_val).strip() not in ['I', 'II']:
            return str(model_val).strip()
        # Generate model as diameter-lead if both are available
        diameter_val = row.get('外徑')
        lead_val = row.get('導程')
        if diameter_val and lead_val:
            try:
                diameter = str(int(float(diameter_val)))
                lead = str(int(float(lead_val)))
                return f"{diameter}-{lead}"
            except (ValueError, TypeError):
                pass
        return model_val if model_val and str(model_val).strip() else None
    
    output_df['型號'] = output_df.apply(generate_model_number, axis=1)
    
    # Convert numeric columns but keep original values for semantic text
    numeric_cols = ['外徑', '導程', '動負荷', '靜負荷', '剛性']
    for col in numeric_cols:
        if col in output_df.columns:
            # Store original values before conversion
            orig_col = f"{col}_orig"
            output_df[orig_col] = output_df[col]
            # Keep as string for Excel, don't convert to numeric
            output_df[col] = output_df[col].fillna('').astype(str).str.strip().replace('', None)
    
    output_df = output_df.dropna(how='all', subset=['外徑', '導程', '動負荷', '靜負荷', '剛性']).reset_index(drop=True)
    
    print(f"  Returning {len(output_df)} rows")
    
    return output_df if not output_df.empty else None
    """Generate semantic description"""
    try:
        series = row.get('Series_Name', 'N/A')
        model = row.get('型號', 'N/A')
        
        # Use original values for display
        diameter = row.get('外徑_orig', row.get('外徑', 'N/A'))
        lead = row.get('導程_orig', row.get('導程', 'N/A'))
        dynamic_load = row.get('動負荷_orig', row.get('動負荷', 'N/A'))
        static_load = row.get('靜負荷_orig', row.get('靜負荷', 'N/A'))
        rigidity = row.get('剛性_orig', row.get('剛性', 'N/A'))
        
        return (
            f"PMI滾珠螺桿規格。系列: {series}, 型號: {model}。"
            f"外徑: {diameter}mm, 導程: {lead}mm。"
            f"動負荷: {dynamic_load}kgf, 靜負荷: {static_load}kgf, 剛性: {rigidity}kgf/umk。"
        )
    except Exception as e:
        return f"PMI滾珠螺桿規格。系列: {row.get('Series_Name', 'N/A')}, 型號: {row.get('型號', 'N/A')}。"
        return "Error generating semantic text"


def extract_all_pmi_tables(pdf_path):
    """Extract all PMI tables from PDF"""
    all_data = []
    last_series = "Unknown"
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_idx, page in enumerate(pdf.pages):
            print(f"Page {page_idx + 1:2d}...", end="", flush=True)
            
            text = page.extract_text()
            series_name = extract_series_name(text)
            if series_name != "Unknown":
                last_series = series_name
            else:
                series_name = last_series
            
            tables = page.extract_tables({
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
                "snap_tolerance": 3,
                "join_tolerance": 3,
            })
            
            if not tables:
                print(" [no tables]")
                continue
            
            table_count = 0
            row_count = 0
            
            for table in tables:
                result = process_pdf_table(table, series_name, page_idx)
                if result is not None and not result.empty:
                    all_data.append(result)
                    table_count += 1
                    row_count += len(result)
            
            if table_count > 0:
                print(f" [{table_count} table(s), {row_count} row(s)]")
            else:
                print(" [no valid tables]")
    
    if not all_data:
        return None
    
    final_df = pd.concat(all_data, ignore_index=True)
    final_df['semantic_text'] = final_df.apply(generate_semantic_text, axis=1)
    
    # Select only the columns we want to save
    columns_to_save = ['Series_Name', 'Source_Page', '型號', '外徑', '導程', '動負荷', '靜負荷', '剛性', 'semantic_text']
    final_df = final_df[columns_to_save]
    
    return final_df


if __name__ == '__main__':
    pdf_path = r"C:\Users\e11338\Desktop\銀泰目錄分割\銀泰螺桿型錄 切割 共67頁.pdf"
    
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "PMI_Final_Data_V3.xlsx"
    
    print("=" * 60)
    print("PMI Catalog Extraction")
    print("=" * 60)
    print(f"PDF: {pdf_path}")
    print(f"Output: {output_file}\n")
    
    final_df = extract_all_pmi_tables(pdf_path)
    
    print("\n" + "=" * 60)
    
    if final_df is not None and not final_df.empty:
        print(f"✓ Extraction Complete!")
        print(f"Total rows: {len(final_df)}")
        print(f"Columns: {final_df.columns.tolist()}")
        print(f"\nSample (first 5 rows):")
        print(final_df.head(5))
        
        try:
            final_df.to_excel(output_file, index=False)
            print(f"\n✓ Successfully saved to: {output_file}")
        except Exception as e:
            print(f"\n✗ Error saving: {e}")
    else:
        print("✗ Failed to extract data")
    
    print("=" * 60)
