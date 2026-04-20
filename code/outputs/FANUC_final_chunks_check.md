# PMI 型錄文字擷取結果檢視

**總計擷取頁數:** 290

---

## 第 2 頁
**本頁字數:** 1154 字

### 內容摘要:
```text
 No part of this manual may be reproduced in any form. 
 The appearance and specifications of this product are subject to change without notice.

The products in this manual are controlled based on Japan's “Foreign Exchange and Foreign Trade Law". The export 
from Japan may be subject to an export license by the government of Japan. Further, re-export to another country may 
be subject to the license of the government of the country from where the product is re-exported. Furthermore, the 
product may also be controlled by re-export regulations of the United States government. Should you wish to export or 
re-export these products, please contact FANUC for advice.

In this manual, we endeavor to include all pertinent matters.

e-export these products, please contact FANUC for advice.

In this manual, we endeavor to include all pertinent matters. 
There are, however, a very large number of operations that must not or cannot be performed, and if the manual 
contained them all, it would be enormous in volume. 
It is, therefore, requested to assume that any operations that are not explicitly described as being possible are "not 
possible".
```

---

## 第 3 頁
**本頁字數:** 898 字

### 內容摘要:
```text
Safety precautions 
iii 
Safety precautions 
This "Safety Precautions" section describes the precautions which must be observed to ensure safety when using 
FANUC servo motors. Users of any servo motor model are requested to read this "Safety Precautions" carefully 
before using the servo motor. 
Users are also requested to read this manual carefully and understand each function of the motor for correct use. 
Users are basically forbidden to do any behavior or action not mentioned in the "Safety Precautions." 
Users are invited to ask FANUC previously about the behavior or action not mentioned here. 
Definition of warning, caution, and note 
This manual includes safety precautions for protecting users and preventing damage to the machine. Precautions are 
classified into warnings and cautions according to their bearing on safety. 
Also, supplementary information is described as a Note.
```

---

## 第 3 頁
**本頁字數:** 954 字

### 內容摘要:
```text
nto warnings and cautions according to their bearing on safety. 
Also, supplementary information is described as a Note. 
Read all warnings, cautions, and notes thoroughly before using the machine.

Used if a danger resulting in the death or serious injury of the user is expected to occur if he or she fails to observe the 
approved procedure.

Used if a danger resulting in the minor or moderate injury of the user or equipment damage is expected to occur if he or 
she fails to observe the approved procedure.

NOTE 
Used if a supplementary explanation not related to any of WARNING and CAUTION is to be indicated.

Even if an item is described in Caution, failure to observe it may lead to a serious result, depending on the situation. 
Each description of Caution provides important information.

t may lead to a serious result, depending on the situation. 
Each description of Caution provides important information. So, be sure to observe Caution.
```

---

## 第 4 頁
**本頁字數:** 765 字

### 內容摘要:
```text
iv 
Warning 
 Be sure to ground a motor frame. 
To avoid electric shocks, ensure that the motor is grounded properly.

 Before starting to connect a motor to electric wires, make sure they are isolated from a power supply. 
You may get electric shocks.

 Do not ground a motor power line terminal or short-circuit it to another power line terminal. 
A failure to observe this may cause electric shocks or a burned winding. 
* 
Some motors require a special connection. Refer to "I.3.2. Outline drawings(P.117)" for details.

 When connecting a cord such as a power line to the terminal block, use the specified tightening torque to firmly 
connect the cord. 
If operation is performed with a loose terminal, the terminal block can overheat, resulting in a fire.
```

---

## 第 4 頁
**本頁字數:** 887 字

### 內容摘要:
```text
onnect the cord. 
If operation is performed with a loose terminal, the terminal block can overheat, resulting in a fire. Moreover, a 
terminal can be detached, resulting in a ground fault, short circuit, or electric shock.

 Do not apply current when a terminal of the terminal block or the crimp terminal of a power line is exposed. 
If a hand or a conductive object touches a terminal of the terminal block or the crimp terminal of a power line, you 
may get electric shocks. Attach an insulation cover (accessory) onto the terminal block. Moreover, cover the crimp 
terminal at the tip of a power line with an insulation tube.

 Assemble and install a connector securely. 
If a power line is detached due to a failure in crimping or soldering, or a conductive area is exposed due to a 
failure in shell assembly, you may get electric shocks.

 Do not touch a motor with a wet hand.
```

---

## 第 4 頁
**本頁字數:** 753 字

### 內容摘要:
```text
ea is exposed due to a 
failure in shell assembly, you may get electric shocks.

 Do not touch a motor with a wet hand. 
You may get electric shocks.

 Before touching a motor, cut off power supply to it. 
Even if a motor is not rotating, it is dangerous as there may be a voltage across the terminals of the motor. 
Especially before touching a power supply connection, take sufficient precautions. Otherwise you may get electric 
shocks.

 Do not touch any terminal of a motor for a while (at least 20 minutes) after the power supply to the motor is cut off. 
High voltage remains across power line terminals of a motor for a while after the power supply to the motor is cut 
off. So, do not touch any terminal or connect it to any other equipment.
```

---

## 第 4 頁
**本頁字數:** 768 字

### 內容摘要:
```text
ile after the power supply to the motor is cut 
off. So, do not touch any terminal or connect it to any other equipment. Otherwise, you may get electric shocks or 
the motor and/or equipment may get damaged.

 Do not overload an integrated brake exceeding the brake torque. 
It may lead to serious accidents as the integrated brake fails to hold the shaft. (Fall of spindle head, etc.)

 On the machine, install a stop device for securing safety. 
The brake built into the servo motor is not a stop device for securing safety. The machine may not be held if a 
failure occurs.

 Do not enter the area under the vertical axis without securing safety. 
If the vertical axis drops unexpectedly, you may be injured.

 Fasten a motor firmly before activating the motor.
```

---

## 第 4 頁
**本頁字數:** 768 字

### 內容摘要:
```text
ety. 
If the vertical axis drops unexpectedly, you may be injured.

 Fasten a motor firmly before activating the motor. 
If a motor is activated when the motor is not fastened firmly or is fastened insufficiently, the motor can tumble or 
come off completely. If the motor mounting section is not sufficiently strong, the machine may be damaged or the 
user may be injured.

 Do not get close to or touch a rotary section of a motor when it is rotating. 
When a motor is rotating, clothes or fingers can be caught, resulting in an injury.

 Do not insert fingers or sticks into a fan motor. 
Although a cover is set for a fan motor, users may be injured if fingers or sticks are inserted when the fan motor is 
rotating.

e inserted when the fan motor is 
rotating.
```

---

## 第 5 頁
**本頁字數:** 717 字

### 內容摘要:
```text
 Do not activate a motor with an object such as a key exposed. 
The object such as a key can fly off, resulting in an injury. Before rotating a motor, check that there is no object 
that can fly off by motor rotation.

 Do not apply a radial load exceeding the "allowable radial load" to a shaft. 
The shaft can break, and parts can fly off. When the vertical axis is involved, the vertical axis may drop.

 To operate a motor, use a specified amplifier and parameters. 
An incorrect combination of a motor, amplifier, and parameters may cause the motor to behave unexpectedly. This 
is dangerous, and the motor may get damaged.

 Operate a motor at a load inertia moment ratio not higher than a prescribed level.
```

---

## 第 5 頁
**本頁字數:** 861 字

### 內容摘要:
```text
us, and the motor may get damaged.

 Operate a motor at a load inertia moment ratio not higher than a prescribed level. 
If a dynamic brake is applied at a load inertia moment ratio higher than a prescribed level, abnormal heat 
generation may occur in a resistor element, resulting in an amplifier or dynamic brake module being burned or 
causing a fire.

 Make sure that the motor will not be rotated by an external force in the event of an alarm or emergency stop. 
In the event of an alarm or emergency stop, the servo amplifier activates the dynamic brake circuit. If the servo 
motor is rotated by an external force with the dynamic brake circuit activated, the servo amplifier and/or dynamic 
brake module may overheat, resulting in a fire.

 Do not bring any hazardous material near a motor. 
Motors are connected to a power circuit, and may get hot.
```

---

## 第 5 頁
**本頁字數:** 753 字

### 內容摘要:
```text
a fire.

 Do not bring any hazardous material near a motor. 
Motors are connected to a power circuit, and may get hot. If flammables or flammable gas is placed near a motor, 
they may be ignited, catch fire, or explode.

 Be safely dressed when handling a motor. 
You may get injured by edges or protrusions, or get electric shocks. Wear safety shoes or gloves to secure safety.

 Use devices such as a crane to move a motor from one place to another. 
A motor is heavy, so if you lift it by hand, you may be exposed to various risks such as injuring your back or getting 
seriously injured by dropping the motor. Use devices such as a crane as needed. (For the weight of a motor, see 
"I. specifications(P.1).")

tor, see 
"I. specifications(P.1).")
```

---

## 第 6 頁
**本頁字數:** 874 字

### 內容摘要:
```text
vi 
Caution 
 Do not touch a motor when it is running or immediately after it stops. 
A motor may get hot when it is running. Do not touch the motor until it gets cool enough. Otherwise, you may get 
burned.

 Be careful not to get your hair or clothes caught in a fan motor. 
Be careful especially when the cooling fan motor is generating an inward air flow. Be careful also for a fan even 
when the motor is stopped, as the fan motor continues to rotate while the amplifier is turned on.

 Make sure that the phase rotation is correct when connecting fan motor to a power supply. 
If the phase rotation of the fan motor's power supply connection is incorrect for models with a cooling fan, the fan 
motor rotates counterclockwise. This may result in a decline in efficiency or cause the fan motor to stop from 
overheating.

 Install the parts around a motor securely.
```

---

## 第 6 頁
**本頁字數:** 788 字

### 內容摘要:
```text
a decline in efficiency or cause the fan motor to stop from 
overheating.

 Install the parts around a motor securely. 
If a component is displaced or removed during motor rotation, a danger can result.

 Use the eyebolt of a motor only to move the motor. 
When a motor is installed on a machine, do not move the machine by using the eyebolt of the motor. Otherwise, 
the eyebolt and/or motor can be damaged.

 Do not disassemble a motor. 
Disassembling a motor may cause a failure or trouble in it. If disassembly is in need for maintenance, please 
contact FANUC. For Pulsecoder replacement, refer to maintenance manual (B-65555EN).

 Do not machine or modify a motor. 
Do not machine or modify a motor in any case except when motor machining or modification is specified by 
FANUC.
```

---

## 第 6 頁
**本頁字數:** 843 字

### 內容摘要:
```text
motor. 
Do not machine or modify a motor in any case except when motor machining or modification is specified by 
FANUC. Modifying a motor may cause a failure or trouble in it.

 Do not conduct dielectric strength test or insulation test (megger test) for a detector. 
Such a test can damage elements in the detector.

 Be sure to connect motor cables correctly. 
An incorrect connection of a cable cause abnormal heat generation, equipment malfunction, or failure. Always use 
a cable with an appropriate current carrying capacity (or thickness) and withstand voltage. Refer to "I.3.2. Outline 
drawings(P.117) " for details on connection.

 Do not apply shocks to a motor or cause scratches to it. 
If a motor is subjected to shocks or is scratched, its components may be adversely affected, resulting in normal 
operation being impaired.
```

---

## 第 6 頁
**本頁字數:** 836 字

### 內容摘要:
```text
cted to shocks or is scratched, its components may be adversely affected, resulting in normal 
operation being impaired. Plastic components, sensors, and power connectors of a servo motor can be damaged 
easily. Handle them very carefully. 
In particular, do not lift a motor by using a plastic component, connector, terminal box, and so forth.

 Do not step or sit on a motor, and do not put a heavy object on a motor. 
The motor may get deformed or be broken. Do not put a motor on another unless they are in packages.

 When attaching a component having inertia, such as a pulley, to a shaft, ensure that any imbalance between the 
shaft and the component is minimized. 
If there is a large imbalance, the motor may vibrates abnormally, resulting in the motor being broken.

 Be sure to attach a key to a motor with a keyed shaft.
```

---

## 第 6 頁
**本頁字數:** 558 字

### 內容摘要:
```text
may vibrates abnormally, resulting in the motor being broken.

 Be sure to attach a key to a motor with a keyed shaft. 
If a motor with a keyed shaft runs with no key attached, it may impair torque transmission or cause imbalance, 
resulting in the motor being broken.

 Use a motor under an appropriate environment and condition. 
Using a motor in an adverse environment or condition may cause a failure or trouble in it. Refer to "III. Handling, 
installation, and use environment of the motor(P.231) " for details on usage environment and use condition.
```

---

## 第 7 頁
**本頁字數:** 767 字

### 內容摘要:
```text
Safety precautions 
vii 
 Note that IP67 satisfies the provisions for short-time water immersion, and do not guarantee their waterproof 
performance in an atmosphere in which the cutting fluid is applied directly to the motor. 
If cutting fluid or lubricant spills on the motor, it will adversely affect the sealing properties of the motor surface, 
entering the inside of the motor and possibly damaging the motor. Make sure that the motor surface is never wet 
with cutting fluid or lubricant, and also make sure that no fluid builds up around the motor. Always set a cover 
when the motor could get wet.

 Do not apply a commercial power supply directly to a motor. 
Applying a commercial power supply directly to a motor may result in its windings being burned.
```

---

## 第 7 頁
**本頁字數:** 810 字

### 內容摘要:
```text
ly directly to a motor. 
Applying a commercial power supply directly to a motor may result in its windings being burned. Be sure to use a 
specified amplifier for supplying voltage to the motor.

 Do not operate a motor without the integrated brake released. 
The integrated brake may be damaged and the machine may not be held. Moreover, the motor may overheat.

 Do not use the integrated brake for servo motor for braking. 
The brake built into a servo motor is designed for holding. If the brake is used for braking, a failure can occur.

 Ensure that motors are cooled for those requiring forcible cooling. 
If a motor that requires forcible cooling is not cooled normally, it may cause a failure or trouble. For a motor with a 
cooling fan, ensure that it is not clogged or blocked with dust and dirt.
```

---

## 第 7 頁
**本頁字數:** 823 字

### 內容摘要:
```text
ause a failure or trouble. For a motor with a 
cooling fan, ensure that it is not clogged or blocked with dust and dirt. For a liquid cooled motor, ensure that the 
amount of the liquid is appropriate and that the liquid piping is not clogged. For both types, perform regular 
cleaning and inspection.

 When storing a motor, put it in a dry (non-condensing) place at room temperature (0 to 40°C). 
Do not store the motor in places listed below as the motor may be damaged or rust. 
- Places with high humidity so condensation will form. 
- Places with extreme temperature changes. 
- Places always exposed to vibration. (The bearing may be damaged.) 
- Places with much trash and dust. 
In case of long-term storage, apply antirust oil on the machining surface of shafts and other parts regardless of 
storage conditions.
```

---

## 第 7 頁
**本頁字數:** 469 字

### 內容摘要:
```text
g-term storage, apply antirust oil on the machining surface of shafts and other parts regardless of 
storage conditions. 
In addition, keep a motor in such a position that its shaft is held horizontal and its terminal box is at the top.

 FANUC motors are designed for use with machines. Do not use them for other purposes. 
If they are used for an unintended purpose, it may cause an unexpected symptom or trouble. Contact FANUC 
before using them for other purposes.
```

---

## 第 8 頁
**本頁字數:** 892 字

### 內容摘要:
```text
viii 
Note 
NOTE 
 Ensure that a base or frame on which a motor is mounted is strong enough. 
Motors are heavy. If a base or frame on which a motor is mounted is not strong enough, it will cause problems 
such as failing to achieve the required accuracy.

 Do not remove the nameplate from a motor. 
If it comes off, make sure not to lose it. If it is lost and the model becomes unidentifiable, the motor may not be 
able to go through maintenance.

 When testing the winding or insulation resistance of a motor, satisfy the conditions stipulated in IEC60034. 
Testing a motor under a condition severer than those specified in IEC60034 may damage the motor.

 For models with a terminal box, make a conduit hole for the terminal box in a specified position. 
For models that need a conduit hole to be made, be careful not to break or damage unspecified portions. 
For details, see "I.3.2.
```

---

## 第 8 頁
**本頁字數:** 804 字

### 內容摘要:
```text
s that need a conduit hole to be made, be careful not to break or damage unspecified portions. 
For details, see "I.3.2. Outline drawings(P.117)."

 Before using a motor, measure its winding and insulation resistances, and make sure they are normal. 
Especially for a motor that has been stored for a prolonged period of time, make sure to conduct these checks. A 
motor may deteriorate depending on the condition under which it is stored or the time during which it is stored. For 
values on winding resistances, refer to “I. specifications(P.1)" or ask FANUC. For values on insulation resistances, 
see the following table. 
If a motor-installed machine had not been running for a long period of time, confirming insulation resistance using 
αi-D amplifier's Leakage Detection Function is recommended.
```

---

## 第 8 頁
**本頁字數:** 686 字

### 內容摘要:
```text
long period of time, confirming insulation resistance using 
αi-D amplifier's Leakage Detection Function is recommended. Insulation resistance between the motor's winding 
and frame can be measured without removing the motor itself or the motor's power line. Refer to "SERVO 
AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN) or contact FANUC for details.

 To use a motor as long as possible, perform periodic maintenance and inspection for it, and measure its winding 
and insulation resistances. 
Note that excessive inspections (such as dielectric strength tests) of a motor may damage its windings. For values 
on winding resistances, refer to “I. specifications(P.1)" or ask FANUC.
```

---

## 第 8 頁
**本頁字數:** 1012 字

### 內容摘要:
```text
of a motor may damage its windings. For values 
on winding resistances, refer to “I. specifications(P.1)" or ask FANUC. For values on insulation resistances, see the 
following table.

Motor insulation resistance measurement 
Measure insulation resistance between each winding and motor frame using an insulation resistance meter 
(DC500V). Judge the measurements according to the following table. Make an insulation resistance measurement on 
a single motor unit after detaching cords such as a power line.

Insulation 
resistance 
Judgment 
100 MΩ or higher 
Acceptable 
10 to 100 MΩ 
The winding has begun deteriorating. There is no problem with the performance at present. Be 
sure to perform periodic inspection. 
1 to 10 MΩ 
The winding has considerably deteriorated. Special care is in need. Be sure to perform periodic 
inspection. 
Lower than 1 MΩ 
Unacceptable.

iderably deteriorated. Special care is in need. Be sure to perform periodic 
inspection. 
Lower than 1 MΩ 
Unacceptable. Replace the motor.
```

---

## 第 9 頁
**本頁字數:** 1109 字

### 內容摘要:
```text
Safety precautions 
ix 
Caution label 
The following label is attached to the motor. 
Attach this label to a prominent place on the motor to call attention to users.

Heat caution label 
Since the motor is heated to a high temperature during operation or immediately after a stop, touching the motor may 
cause a burn. So, attach this label to a prominent place to call attention when the motor surface is exposed and may 
be touched.

Remarks: 
The mark of this label conforms to the IEC standard. 
The mark has the meaning of heat caution, so the description is omitted.

Electric shock caution label 
This label indicates the risk of electric shock. Before installing the motor or performing maintenance work, turn off the 
power supply.

ates the risk of electric shock. Before installing the motor or performing maintenance work, turn off the 
power supply. Attach this label to a prominent place on the motor, such as on the upper lid of the terminal box.

Remarks: 
The mark of this label conforms to the IEC standard. 
The mark has the meaning of electric shock caution, so the description is omitted.
```

---

## 第 10 頁
**本頁字數:** 528 字

### 內容摘要:
```text
x 
Shipping the servo motor by air 
Although the servo motors described in this manual contain magnets in their rotor, the magnetic circuit is closed 
between the rotor and stator, so they do not fall under "magnetized material" (which has a maximum magnetic field 
strength sufficient to cause a compass deflection of more than 2 degrees at a distance of 2.1 m from any point on the 
surface of the package) defined in the IATA Dangerous Goods Regulations. 
The assembled servo motor can be transported by air as general cargo.
```

---

## 第 11 頁
**本頁字數:** 643 字

### 內容摘要:
```text
Preface 
xi 
Preface 
This manual describes the specifications, outline drawings, detectors and other options, usage, and selection method 
of the FANUC SERVO MOTOR αi-D series (αiS-D, αiF-D series). 
Make sure you understand the instructions provided herein before using a servo motor. 
In this manual, servo motor names are sometimes abbreviated as follows: 
Example: αiS 30/4000-D → αiS 30-D 
This manual describes the layout of power pins and the output of detector signals but does not provide information 
about connection to a servo amplifier and a CNC. 
For information about the connection, refer to the relevant manuals listed below.
```

---

## 第 11 頁
**本頁字數:** 601 字

### 內容摘要:
```text
f amplifier 
Provided

"SERVO MOTOR αi-D series, SPINDLE MOTOR 
αi-D series, SERVO AMPLIFIER αi-D series 
MAINTENANCE MANUAL" (B-65555EN)

• Startup 
procedure 
• Troubleshooting 
• Maintenance of 
motor 
• System 
setup 
(Hardware) 
• 
Troubleshooti
ng 
• Maintenance 
of motor 
Provided

"AC SERVO MOTOR αi-B/αi/βi-B/βi series, 
LINEAR MOTOR LiS-B/LiS series, DD MOTOR 
DiS-B/DiS series PARAMETER MANUAL" (B-
65270EN)

• Initial setting 
• Parameter 
setting 
• Description of 
parameters 
• System 
setup 
(Software) 
• System 
tuning 
(Parameters)

Read this manual thoroughly and keep it at hand.
```

---

## 第 17 頁
**本頁字數:** 800 字

### 內容摘要:
```text
Lineup of the series 
3 
1. 
Lineup of the series

1.1. 
Motor Lineup 
The FANUC SERVO MOTOR αi-D series consist of the following series, each of which has the listed features. 
Series 
Voltage 
Feature 
Applications 
αiS-D 
200V 
High speed and high acceleration feed axes 
Feed axes in machine tools 
Peripherals of machine tools 
Industrial machines 
400V 
Direct connection to a 400-V power supply 
αiF-D 
200V 
Extremely high smoothness of feed 
Feed axes in machine tools 
Industrial machines 
400V 
Direct connection to a 400-V power supply 
Lineup 
Continuous 
torque 
(at low speed) 
Nm 
0.16 
0.32 
0.65 
1.2 
1.6 
2 
4 
8 
12 
18 
22 
30 
40 
50 
60 
Flange size 
mm 
40 
60 
90 
130 
174 
αiS-D 
200V 
αiS 0.2 
/8000-D 
αiS 0.3 
/8000-D 
αiS 0.5 
/8000-D 
αiS 1 
/8000-D 
αiS 1.5 
/8000-D
```

---

## 第 18 頁
**本頁字數:** 777 字

### 內容摘要:
```text
4 
1.2. 
Feature 
The FANUC SERVO MOTOR αi-D series are the perfect servo motor for machine tool and industrial machine feed 
axis applications. Their acceleration performance has improved with the enhanced speed-torque characteristics to 
shorten cycle time compared to FANUC's conventional product (Note 1). Moreover, the extremely high smoothness of 
feed enhanced by decreasing cogging torque and with the latest control enables the product to achieve higher 
accuracy and quality.

Motor feature suitable for use 
αiS-D : 
Achieves high acceleration by the high torque characteristics with the adoption of the latest neodymium magnet. This 
is the standard series of FANUC servo motors suitable for high-speed and high-accuracy machining with its high 
smoothness of feed.
```

---

## 第 18 頁
**本頁字數:** 686 字

### 內容摘要:
```text
dard series of FANUC servo motors suitable for high-speed and high-accuracy machining with its high 
smoothness of feed. 
αiF-D : 
A product with an extremely small cogging torque and high moment of inertia of rotor achieved by adopting the latest 
ferrite magnet. Excellent controllability and strength against disturbance. This is the FANUC servo motors suitable for 
high-accuracy, high-quality machining with an extremely high smoothness of feed.

Smooth feed 
Compared to FANUC's conventional product (Note 1), cogging torque has been reduced to a maximum of about a 
third, and responsiveness has been improved with speed-enhanced Pulsecoder communication and the latest 
control.
```

---

## 第 18 頁
**本頁字數:** 474 字

### 內容摘要:
```text
out a 
third, and responsiveness has been improved with speed-enhanced Pulsecoder communication and the latest 
control. With these state-of-the-art technologies, αi-D series achieves the highest smoothness of feed in our history.

Enhanced speed-torque characteristics 
Compared to FANUC's conventional product (Note 1), the speed-torque characteristics are improved by adopting a 
new rotor structure and the latest magnet, densifying windings, and applying a new control.
```

---

## 第 18 頁
**本頁字數:** 875 字

### 內容摘要:
```text
are improved by adopting a 
new rotor structure and the latest magnet, densifying windings, and applying a new control. Moreover, a control using 
DC link voltage information minimizes a torque reduction when DC link voltage drops and heating while high-speed 
rotation.

Excellent waterproof 
Our unique form and sealing structure achieves Ingress Protection IP67.

Energy saving 
Compared to FANUC's conventional product (Note 1), a new magnetic design and control aim to reduce loss, 
contributing to energy saving.

Built-in, high-accuracy encoder 
A high-accuracy positioning is achieved with an integrated optical encoder (Pulsecoder) with a high resolution of up to 
32,000,000 [division/revolution]. The battery-less type, which does not require battery replacement, is also available.

Integrated holding brake 
An integrated holding brake is available as an option.
```

---

## 第 18 頁
**本頁字數:** 680 字

### 內容摘要:
```text
attery replacement, is also available.

Integrated holding brake 
An integrated holding brake is available as an option. 
A reduced backlash brake is also available. (Note: αiS 22-D to αiS 60-D,αiF 12-D to αiF 40-D)

Power connector 
The use of connectors that can be attached with a single touch allows for easy cable connection. The connector 
alone is IP67. (Note: αiS 0.5 to 60-D, αiF 1 to 40-D)

Interchangeability (Note 2) 
The shape of parts such as flanges and shafts are compatible with our conventional products (Note 1), making 
replacement easy. 
NOTE 
1. FANUC AC SERVO MOTOR αi-B/βi-B series 
2. Power connectors of ○60 and ○90 models have been changed from Model B.
```

---

## 第 19 頁
**本頁字數:** 800 字

### 內容摘要:
```text
Lineup of the series 
5 
1.3. 
Supported CNC system software, servo control software 
FANUC SERVO MOTOR αi-D series need CNC system software and servo control software listed below to operate. 
It will not operate using unsupported CNC system software and servo control software.

Supported CNC system software 
CNC 
CNC system software 
Series 
Version 
FS30i-B Plus 
G307, G317, G327, G337, G357 
Version 03 or later 
FS30i-B5 Plus 
G427, G42E, G437, G487, G4H7 
Version 03 or later 
FS31i-B Plus 
G407, G40E, G417, G457, G4G7 
Version 03 or later 
FS32i-B Plus 
G507, G517, G527 
Version 03 or later 
FS30i-LB Plus 
G3C7, G3D7, G3C8, G3D8 
Version 01 or later 
FS31i-LB Plus 
G4B7, G4C7, G4B8, G4C8 
Version 01 or later 
FS0i-F Plus 
D4G3, D6G3 
Version 11 or later 
FS0i-LF Plus 
DCG3, DCG4 
Vers
```

---

## 第 19 頁
**本頁字數:** 559 字

### 內容摘要:
```text
4B7, G4C7, G4B8, G4C8 
Version 01 or later 
FS0i-F Plus 
D4G3, D6G3 
Version 11 or later 
FS0i-LF Plus 
DCG3, DCG4 
Version 01 or later 
Power Motion i-A 
88H0 
Version 43 or later 
DSA-B 
881W 
Version 04 or later

Supported servo control software 
CNC 
Servo control software 
Series 
Version 
30i-B Plus Series 
90J0 
90J3 
Version 27.0 or later 
Version 18.0 or later 
0i-F Plus Series 
90J5 
90J7 
Version 12.0 or later 
Version 11.0 or later 
Power Motion i-A 
90J0 
90JP 
Version 27.0 or later 
Version 11.0 or later 
DSA-B 
90JP 
Version 11.0 or later
```

---

## 第 20 頁
**本頁字數:** 612 字

### 內容摘要:
```text
Ordering specification numbers

6 
2. 
Ordering specification numbers 
The ordering specification numbers of the servo motors have the following format:

○○○○ 
An ordering specification number is described on the following pages. 
NOTE 
Not all combinations exist.

△ 
0 : Taper shaft 
1 : Straight shaft 
2 : Straight shaft with a key way 
3 : Taper shaft with a 24VDC brake 
4 : Straight shaft with a 24VDC brake 
5 : Straight shaft with a key way and a 24VDC brake 
NOTE 
Do not select "Straight shaft with a key way" when a large torque or abrupt acceleration rate is required.

Brake types are listed below.
```

---

## 第 20 頁
**本頁字數:** 679 字

### 內容摘要:
```text
raight shaft with a key way" when a large torque or abrupt acceleration rate is required.

Brake types are listed below. 
αiS 0.2-D, αiS 0.3-D:0.32Nm brake 
αiS 0.5-D:0.65Nm brake 
αiS 1-D: 1.2Nm brake 
αiS 1.5-D:1.6Nm brake 
αiS 2-D, αiS 4-D, αiF 1-D, αiF 2-D :3Nm brake 
αiS 8-D, αiF 4-D, αiF 8-D:8Nm brake 
αiS 12-D, αiS 18-D:12Nm brake 
αiS 22-D to αiS 40-D, αiF 12-D to αiF 40-D:35Nm brake (standard version) 
αiS 40-D to αiS 60-D, αiS 50 FAN-D, αiS 60 FAN-D, αiF 40-D, αiF 40 FAN-D: 70Nm brake (reduced backlash 
version)

○ 
0 : Standard 
1 : With cooling fan 
2 : With 70Nm brake (reduced backlash version) 
3 : With 70Nm brake (reduced backlash version), and cooling fan
```

---

## 第 21 頁
**本頁字數:** 968 字

### 內容摘要:
```text
Ordering specification numbers 
7 
NOTE 
 For those with a 70Nm brake (○ = 2 or 3), specify △ = 3 to 8. 
 70Nm brake is only available for reduced backlash version. 
 70Nm brake can be selected for models listed below. 
 αiS 40-D to αiS 60-D, αiS 50 FAN-D, αiS 60 FAN-D, αiF 40-D, αiF 40 FAN-D（including HV）

cd 
00 : Standard 
51 : With cooling fan (rear emission) 
63: φ14 Taper/straight shaft (αiS 2-D, αiF 1-D, αiF 2-D) 
70: With 35Nm brake (reduced backlash version) (αiS 22-D to αiS 40-D, αiF 12-D to αiF 40-D) 
NOTE 
  Omit when #abcd = #0000.  
  Specify △ = 3 to 8 when #abcd = #ab70  
 35Nm brake reduced backlash version can be selected for models listed below.

Specify △ = 3 to 8 when #abcd = #ab70  
 35Nm brake reduced backlash version can be selected for models listed below. 
 αiS 22-D to αiS 40-D, αiF 12-D to αiF 40-D (including HV)

For αiS 0.2-D to αiS 0.3-D, αiS 0.5-D to αiS 1.5-D (including HV), motor temperature information is omitted.
```

---

## 第 28 頁
**本頁字數:** 574 字

### 內容摘要:
```text
14 
3. 
Motor specifications 
3.1. 
Characteristics curves and data sheet 
3.1.1. 
About characteristics curves and data sheet 
The specifications of each motor are described by the characteristics curves and data sheet given below.

Characteristics curves 
The characteristic curves representing the "speed-torque characteristics" and "overload duty characteristics" are 
given for each motor model.

Speed-torque characteristics 
Speed-torque characteristics indicate the relationship between motor generating torque and rotation speed when 
input voltage is 200V or 400V.
```

---

## 第 28 頁
**本頁字數:** 975 字

### 內容摘要:
```text
istics indicate the relationship between motor generating torque and rotation speed when 
input voltage is 200V or 400V. 
In the continuous operating zone, the motor winding temperature and Pulsecoder temperature do not exceed the 
following overheat temperatures when the ambient temperature is 20°C.

 
Motor winding: 140°C 
 
Pulsecoder: 100°C

In the continuous operating zone, the motor can be used continuously with any combination of a rotation speed and a 
torque. In the intermittent operating zone outside the continuous operating zone, the motor can be used intermittently 
within the range of the overload duty characteristics curve. 
In the high-speed operating zone, to operate the motor stably, the current may increase even at no load, depending 
on the speed.

gh-speed operating zone, to operate the motor stably, the current may increase even at no load, depending 
on the speed. 
Each operating zone may fluctuate depending on the motor's input voltage.
```

---

## 第 29 頁
**本頁字數:** 831 字

### 內容摘要:
```text
Motor specifications 
15 
Overload duty 
The overload duty characteristics represent the relationship between the time duty and the ON time (overload time) 
where the motor can be operated with no temperature limit by the overheat or overcurrent (OVC) alarm when the 
motor is used at low speed with a torque exceeding the continuous operating zone (overload toque).

There are two motor temperature limits that determine overload duty curves; one is based on the overheat of the 
motor itself and the other is based on the OVC alarm of the soft thermal function. 
The limit by overheat is represented by a curve in a long overload time range and the limit by an OVC alarm is 
represented by a short overload time range. The overload duty characteristics are represented by the curve that has 
a shorter limit time between the two.
```

---

## 第 29 頁
**本頁字數:** 1090 字

### 內容摘要:
```text
me range. The overload duty characteristics are represented by the curve that has 
a shorter limit time between the two. 
If the motor is in the overload status at a motor rotation speed of about 0min-1, an OVC alarm may be issued for a 
time shorter than described. Note that, since the driving amplifier also contains a thermal protection device, some 
other restrictions may be imposed depending on the use conditions.

Time duty[%]: The ratio of the overload time to the total time of a single cycle 
ON time[s]: The time during which overload torque continues to be applied within a single cycle.

The procedure for determining the time duty and ON time is as follows.

1. Calculating overload ratio 
Overload ratio = overload torque ÷ continuous torque (during at low speed) 
2.

follows.

1. Calculating overload ratio 
Overload ratio = overload torque ÷ continuous torque (during at low speed) 
2. The motor can be operated with the time duty and ON time at any point on or inside the curve corresponding to 
the overload ratio obtained from 1 for the overload duty characteristics.
```

---

## 第 30 頁
**本頁字數:** 718 字

### 內容摘要:
```text
16 
Data sheet 
The data sheet gives the items relating to motor characteristics listed below. 
Each item shows the default settings (±10%).

Continuous torque (at low speed): Tc [Nm] 
Torque that allows the motor to operate continuously at low speed (ambient temperature 20°C) 
Low speed: up to about 200 [min-1]

Continuous current (at low speed): Ic [A(rms)] 
Value obtained by dividing continuous torque (at low speed) Tc by torque constant Kt (ambient temperature 20°C)

Rated output: Pr [kW] 
Maximum output at continuous operating zone (ambient temperature 20°C)

Rated rotation speed: Nr [min-1] 
Maximum rotation speed at continuous operating zone (Note) 
NOTE 
This is not the rotation speed at rated output.
```

---

## 第 30 頁
**本頁字數:** 800 字

### 內容摘要:
```text
in-1] 
Maximum rotation speed at continuous operating zone (Note) 
NOTE 
This is not the rotation speed at rated output. 
Maximum rotation speed: Nmax [min-1] 
Maximum rotation speed at intermittent operating zone

Maximum torque: Tmax [Nm] 
Maximum motor generating torque when combined with applicable servo amplifier (motor temperature 20°C)

Moment of inertia of rotor: Jm [kgm2] [kgfcms2] 
Moment of inertia of the rotor of the motor 
The values for the standard specification with no brake and for the specification with a brake are given.

Torque constant: Kt [Nm/A(rms)] [kgfcm/A(rms)] 
Motor generating torque developed per ampere of phase current [A(rms)] (motor temperature 20°C) 
The torque constant decreases by 0.11% for the αiS-D series and by 0.19% for the αiF-D series according to t
```

---

## 第 30 頁
**本頁字數:** 1058 字

### 內容摘要:
```text
ture 20°C) 
The torque constant decreases by 0.11% for the αiS-D series and by 0.19% for the αiF-D series according to the 
negative temperature coefficient of the magnet material every time the temperature of the magnet increases by 1°C 
after it exceeds 20°C. 
Torque calculated by multiplying a torque constant by a current value may not match the actual motor generating 
torque due to the effects of magnetic saturation or reluctance torque in the maximum torque zone.

Winding resistance: Ra [Ω] 
Resistance between winding terminals of a motor (motor temperature 20°C)

Thermal time constant: tt [min] 
Time required for the winding temperature at rated output to reach 63.2% of the final temperature rise

Static friction: Tf [Nm] [kgfcm] 
Torque required to rotate the rotor with no load

Ma

2% of the final temperature rise

Static friction: Tf [Nm] [kgfcm] 
Torque required to rotate the rotor with no load

Mass: w [kg] 
Mass of the motor 
The values for the standard specification with no brake and for the specification with a brake are given.
```

---

## 第 31 頁
**本頁字數:** 232 字

### 內容摘要:
```text
Motor specifications 
17 
Max. current of servo amp.: Imax [A(peak)] 
Maximum current of servo amplifiers combined (Note) 
NOTE 
To avoid demagnetization of the motor, the maximum current may be limited by a motor control parameter.
```

---

## 第 131 頁
**本頁字數:** 302 字

### 內容摘要:
```text
Motor specifications 
117 
3.2. 
Outline drawings 
This subsection presents outline drawings of the FANUC SERVO MOTOR αi-D series. 
The shaft shape, allowable axis load, shaft run-out accuracy, and power pin layout are also shown. 
3.2.1. 
Models αiS 0.2-D, αiS 0.3-D 
(1) Outline drawing of the motors
```

---

## 第 132 頁
**本頁字數:** 153 字

### 內容摘要:
```text
(a) Shaft shape types 
The shaft shape of each model is as follows. 
Model 
Straight shaft 
Straight shaft 
with key groove 
αiS 0.2-D, αiS 0.3-D 
φ8 
φ8
```

---

## 第 133 頁
**本頁字數:** 442 字

### 內容摘要:
```text
Motor specifications 
119 
(b) Shaft details

- φ8 straight shaft with a key groove

(3) Allowable axis load 
The allowable axis load is indicated below. 
If a load exceeding the allowable axis load is applied, the bearing or shaft may be damaged. 
For details about allowable axis load, see "III.2. Mounting a servo motor(P.234)." 
Radial load 
Axial load 
(Reference) 
Front bearing specification 
63[N] 
(6.4 [kgf]) 
39[N] 
(4 [kgf]) 
6900
```

---

## 第 134 頁
**本頁字數:** 861 字

### 內容摘要:
```text
120 
(4) Shaft run-out accuracy 
The shaft run-out acuracy is indicated below. 
For details about the shaft run-out accuracy, see "III.2. Mounting a servo motor(P.234)." 
Shaft diameter run-out 
Run-out of the fit surface to the 
shaft center 
Run-out of the flange mounting 
surface to the shaft center 
0.02 mm or less 
0.04 mm or less 
0.06 mm or less

(5) Power connector 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JN14AH04NJ1-F

Power connectors are waterproof when engaged. 
The following shows the shape and pin layout of the power connector. 
For the connected cables and the connectors on the cable side, see "II.1.3.2. Power connectors(P.180)."

(6) Connectors for the brake 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JN4AT02PJ1-R

Brake connectors are waterproof when engaged.
```

---

## 第 134 頁
**本頁字數:** 531 字

### 內容摘要:
```text
facturer specification 
Japan Aviation Electronics Industry 
JN4AT02PJ1-R

Brake connectors are waterproof when engaged. 
The following shows the shape and pin arrangement of the brake connectors. 
Connect the power supply for the brake (24 VDC, 0 V) to BK. The brake is nonpolarized. 
For the connected cables and the connectors on the cable side, see "II.1.3.3. Connectors for the brake(P.186)."

(7) Signal connectors 
For the specifications, shapes, and pin layouts of the signal connectors, see "I.4. Feedback sensors(P.159)."
```

---

## 第 135 頁
**本頁字數:** 237 字

### 內容摘要:
```text
Motor specifications 
121 
3.2.2. 
Models αiS 0.5-D to αiS 1.5-D (including HV) 
(1) Outline drawing of the motors

Model 
A 
B 
C 
αiS 0.5-D, αiS 0.5HV-D 
80 
60 
32 
αiS 1-D, αiS 1HV-D 
101 
81 
53 
αiS 1.5-D, αiS 1.5HV-D 
122 
102 
74
```

---

## 第 137 頁
**本頁字數:** 293 字

### 內容摘要:
```text
Motor specifications 
123 
(2) Shaft shape

(a) Shaft shape types 
The shaft shape of each model is as follows. 
Model 
Straight shaft 
Straight shaft 
with key groove 
 αiS 0.5-D, αiS 0.5HV-D 
φ9 
φ9 
αiS 1-D, αiS 1HV-D, αiS 1.5-D, αiS 1.5HV-D 
φ14 
φ14

- φ9 straight shaft with a key groove
```

---

## 第 138 頁
**本頁字數:** 397 字

### 內容摘要:
```text
- φ14 straight shaft with a key groove

(3) Allowable axis load 
The allowable axis load is indicated below. 
If a load exceeding the allowable axis load is applied, the bearing or shaft may be damaged. 
For details about allowable axis load, see "III.2. Mounting a servo motor(P.234)." 
Radial load 
Axial load 
(Reference) 
Front bearing specification 
196[N] 
(20 [kgf]) 
49[N] 
(5 [kgf]) 
6002
```

---

## 第 139 頁
**本頁字數:** 883 字

### 內容摘要:
```text
Motor specifications 
125 
(4) Shaft run-out accuracy 
The shaft run-out accuracy is indicated below. 
For details about the shaft run-out accuracy, see "III.2. Mounting a servo motor(P.234)." 
Shaft diameter run-out 
Run-out of the fit surface to the shaft 
center 
Run-out of the flange mounting 
surface to the shaft center 
0.02 mm or less 
0.04 mm or less 
0.06 mm or less

(5) Power connector 
Manufacturer 
Manufacturer specification 
Tyco Electronics Japan GK 
2822926-1

Power connectors are waterproof in themselves (unengaged). 
The following shows the shape and pin layout of the power connector. 
For the connected cables and the connectors on the cable side, see "II.1.3.2. Power connectors(P.180)."

(6) Connectors for the brake 
Manufacturer 
Manufacturer specification 
Tyco Electronics Japan GK 
2304867-1

Brake connectors are waterproof in themselves (unengaged).
```

---

## 第 139 頁
**本頁字數:** 531 字

### 內容摘要:
```text
facturer specification 
Tyco Electronics Japan GK 
2304867-1

Brake connectors are waterproof in themselves (unengaged). 
The following shows the shape and pin arrangement of the brake connectors. 
Connect the power supply for the brake (24 VDC, 0 V) to BK. The brake is nonpolarized. 
For the connected cables and the connectors on the cable side, see "II.1.3.3. Connectors for the brake(P.186)."

(7) Signal connectors 
For the specifications, shapes, and pin layouts of the signal connectors, see "I.4. Feedback sensors(P.159)."
```

---

## 第 141 頁
**本頁字數:** 495 字

### 內容摘要:
```text
Motor specifications 
127 
(b) With a brake

Model 
A 
B 
C 
D 
αiS 2-D, αiS 2HV-D, αiF 1-D 
159 
148 
99 
61 
αiS 4-D, αiS 4HV-D, αiF 2-D 
195 
184 
135 
97

(a) Shaft shape types 
The shaft shape of each model is as follows. 
Model 
Taper shaft 
Straight shaft 
Straight shaft 
with key groove 
αiS 2-D, αiS 2HV-D, αiF 1-D, αiF 2-D 
φ11 (φ14) 
φ10 (φ14) 
φ10 (φ14) 
αiS 4-D, αiS 4HV-D 
φ14 
φ14 
φ14 
* 
Shown within parentheses is the option for modification. In case of A06B-○○○○-B△ ○▽ #**63
```

---

## 第 143 頁
**本頁字數:** 127 字

### 內容摘要:
```text
Motor specifications 
129 
- φ14 straight shaft

- φ10 straight shaft with a key groove

- φ14 straight shaft with a key groove
```

---

## 第 144 頁
**本頁字數:** 875 字

### 內容摘要:
```text
130 
(3) Allowable axis load 
The allowable axis load is indicated below. 
If a load exceeding the allowable axis load is applied, the bearing or shaft may be damaged. 
For details about allowable axis load, see "III.2. Mounting a servo motor(P.234)." 
Radial load 
Axial load 
(Reference) 
Front bearing specification 
245[N] 
(25 [kgf]) 
78[N] 
(8 [kgf]) 
6003

(4) Shaft run-out accuracy 
The shaft run-out accuracy is indicated below. 
For details about the shaft run-out accuracy, see "III.2. Mounting a servo motor(P.234)." 
Shaft diameter run-out 
Run-out of the fit surface to the 
shaft center 
Run-out of the flange mounting surface to 
the shaft center 
0.02 mm or less 
0.04 mm or less 
0.05 mm or less

(5) Power connector 
Manufacturer 
Manufacturer specification 
Tyco Electronics Japan GK 
2291721-1

Power connectors are waterproof in themselves (unengaged).
```

---

## 第 144 頁
**本頁字數:** 806 字

### 內容摘要:
```text
facturer specification 
Tyco Electronics Japan GK 
2291721-1

Power connectors are waterproof in themselves (unengaged). 
The following shows the shape and pin layout of the power connector. 
For the connected cables and the connectors on the cable side, see "II.1.3.2. Power connectors(P.180)."

(6) Connectors for the brake 
Manufacturer 
Manufacturer specification 
Tyco Electronics Japan GK 
2304867-1

Brake connectors are waterproof in themselves (unengaged). 
The following shows the shape and pin arrangement of the brake connectors. 
Connect the power supply for the brake (24 VDC, 0 V) to BK. The brake is nonpolarized. 
For the connected cables and the connectors on the cable side, see "II.1.3.3. Connectors for the brake(P.186)."

e cable side, see "II.1.3.3. Connectors for the brake(P.186)."
```

---

## 第 145 頁
**本頁字數:** 132 字

### 內容摘要:
```text
(7) Signal connectors 
For the specifications, shapes, and pin layouts of the signal connectors, see "I.4. Feedback sensors(P.159)."
```

---

## 第 147 頁
**本頁字數:** 484 字

### 內容摘要:
```text
Motor specifications 
133 
(b) With a brake

Model 
A 
B 
C 
αiS 8-D, αiS 8HV-D 
αiF 4-D, αiF 4HV-D 
191 
133 
47 
αiS 12-D, αiS 12HV-D 
αiF 8-D, αiF 8HV-D 
247 
189 
αiS 18-D, αiS 18HV-D 
303 
245

(a) Shaft shape types 
The shaft shape of each model is as follows. 
Model 
Taper shaft 
Straight shaft 
Straight shaft 
with key groove 
αiS 8-D, αiS 8HV-D 
αiF 4-D, αiF 4HV-D 
φ16 
φ19 
φ19 
αiS 12-D, αiS 12HV-D 
αiF 8-D, αiF 8HV-D 
φ16 
φ24 
φ24 
αiS 18-D, αiS 18HV-D 
φ24 
φ24 
φ24
```

---

## 第 148 頁
**本頁字數:** 65 字

### 內容摘要:
```text
- φ16 taper shaft (with a brake)

- φ19 straight shaft (standard)
```

---

## 第 149 頁
**本頁字數:** 164 字

### 內容摘要:
```text
Motor specifications 
135 
- φ19 straight shaft (with a brake)

- φ19 straight shaft with key groove (standard)

- φ19 straight shaft with key groove (with a brake)
```

---

## 第 150 頁
**本頁字數:** 100 字

### 內容摘要:
```text
136 
- φ24 taper shaft (standard)

- φ24 taper shaft (with a brake)

- φ24 straight shaft (standard)
```

---

## 第 151 頁
**本頁字數:** 164 字

### 內容摘要:
```text
Motor specifications 
137 
- φ24 straight shaft (with a brake)

- φ24 straight shaft with key groove (standard)

- φ24 straight shaft with key groove (with a brake)
```

---

## 第 152 頁
**本頁字數:** 814 字

### 內容摘要:
```text
138 
(3) Allowable axis load 
The allowable axis load is indicated below. 
If a load exceeding the allowable axis load is applied, the bearing or shaft may be damaged. 
For details about allowable axis load, see "III.2. Mounting a servo motor(P.234)." 
Radial load 
Axial load 
(Reference) 
Front bearing specification 
686[N] 
(70 [kgf]) 
196[N] 
(20 [kgf]) 
6205

(4) Shaft run-out accuracy 
The shaft run-out accuracy is indicated below. 
For details about the shaft run-out accuracy, see "III.2. Mounting a servo motor(P.234)." 
Shaft diameter run-out 
Run-out of the fit surface to the 
shaft center 
Run-out of the flange mounting 
surface to the shaft center 
0.02 mm or less 
0.04 mm or less 
0.05 mm or less

(5) Power connector 
Types of power connectors 
The power connector of each model is as follows.
```

---

## 第 152 頁
**本頁字數:** 1081 字

### 內容摘要:
```text
less 
0.05 mm or less

(5) Power connector 
Types of power connectors 
The power connector of each model is as follows. 
Model 
Power connector 
All models other than the followings 
MS 18-10P compatible connector 
αiS 12/8000-D 
MS 20-15P compatible connector

・MS18-10P compatible connector 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JL10-2E18-10PE 
Hirose Electric 
H/MSD3102A18-10P-D-T

As the power connector, a receptacle connector having a waterproof property by itself (when it is not engaged) is 
used as standard. 
Either a bayonet-type connector or screw-type connector can be connected. 
Strictly speaking, this power connector does not meet the MS standard, but it can be used as a connector compatible 
with the MS-standard round connector.

ector does not meet the MS standard, but it can be used as a connector compatible 
with the MS-standard round connector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance. 
Contact the manufacturer of the connector in question.
```

---

## 第 153 頁
**本頁字數:** 705 字

### 內容摘要:
```text
Motor specifications 
139 
The following shows the shape and pin layout of the power connector.

- MS20-15P compatible connector 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JL10-2E20-15PE(G)-B

As the power connector, a receptacle connector having a waterproof property by itself (when it is not engaged) is 
used as standard. 
Either a bayonet-type connector or screw-type connector can be connected. 
Strictly speaking, this power connector does not meet the MS standard, but it can be used as a connector compatible 
with the MS-standard round connector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance.
```

---

## 第 153 頁
**本頁字數:** 734 字

### 內容摘要:
```text
nnector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance. 
Contact the manufacturer of the connector in question.

The following shows the shape and pin layout of the power connector.

(6) Connectors for the brake 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JN2AS04MK3-R

Brake connectors are waterproof in themselves (unengaged). 
The following shows the shape and pin arrangement of the brake connectors. 
Connect the power supply for the brake (24 VDC, 0 V) to BK. The brake is nonpolarized. 
For the connected cables and the connectors on the cable side, see "II.1.3.3. Connectors for the brake(P.186)."

ors for the brake(P.186)."
```

---

## 第 154 頁
**本頁字數:** 252 字

### 內容摘要:
```text
NOTE 
No.4 pin is connected to the brake housing. Use it when you need to connect the shield line for the brake cable.

(7) Signal connectors 
For the specifications, shapes, and pin layouts of the signal connectors, see "I.4. Feedback sensors(P.159)."
```

---

## 第 155 頁
**本頁字數:** 154 字

### 內容摘要:
```text
Motor specifications 
141 
3.2.5. 
Models αiS 22-D\~αiS 60 FAN-D (including HV), αiF 12-D\~αiF 40 FAN-D 
(including HV) 
(1) Outline drawing of the motors
```

---

## 第 157 頁
**本頁字數:** 370 字

### 內容摘要:
```text
Motor specifications 
143 
(c) With cooling fan

Model 
A 
B 
C 
D 
E 
αiS 50 FAN-D, αiS 50HV FAN-D 
416 
288 
51 
288

96 
αiS 60 FAN-D, αiS 60HV FAN-D 
αiF 40 FAN-D, αiF 40HV FAN-D 
490 
362 
#0051 (rear exhaust) is also the same size.

The protection breaker for cooling fan is not built into the motor. Prepare such a circuit breaker in the power magnetics 
cabinet.
```

---

## 第 158 頁
**本頁字數:** 442 字

### 內容摘要:
```text
144 
(d) With a cooling fan and brake

Model 
Brake 
A 
B 
C 
D 
E 
αiS 50 FAN-D, αiS 50HV FAN-D 
70Nm 
482 
354 
51 
288

96 
αiS 60 FAN-D, αiS 60HV FAN-D 
αiF 40 FAN-D, αiF 40HV FAN-D 
556 
428 
#0051 (rear exhaust) is also the same size.

The protection breaker for cooling fan is not built into the motor. Prepare such a circuit breaker in the power magnetics 
cabinet.

(a) Shaft shape types 
The shaft shape of each model is as follows.
```

---

## 第 159 頁
**本頁字數:** 500 字

### 內容摘要:
```text
Motor specifications 
145 
Model 
Taper shaft 
Straight shaft 
Straight shaft 
with key groove 
αiS 22-D, αiS 22HV-D 
αiS 30-D, αiS 30HV-D 
αiS 40-D, αiS 40HV-D 
αiF 12-D, αiF 12HV-D 
αiF 22-D, αiF 22HV-D 
φ32 
φ35 
φ35 
αiS 50-D, αiS 50HV-D 
αiS 60-D, αiS 60HV-D 
(including a cooling fan) 
φ38 
φ35 
- 
αiF 30-D, αiF 30HV-D 
αiF 40-D, αiF 40HV-D 
(including a cooling fan) 
φ38 
φ35 
φ35 
* 
Do not select "Straight shaft with a key way" when a large torque or abrupt acceleration rate is required.
```

---

## 第 160 頁
**本頁字數:** 974 字

### 內容摘要:
```text
- φ35 straight shaft with a key groove

(3) Allowable axis load 
The allowable axis load is indicated below. 
If a load exceeding the allowable axis load is applied, the bearing or shaft may be damaged. 
For details about allowable axis load, see "III.2. Mounting a servo motor(P.234)." 
Radial load 
Axial load 
(Reference) 
Front bearing specification 
1960 [N] 
(200 [kgf]) 
588[N] 
(60 [kgf]) 
6208

(4) Shaft run-out accuracy 
The shaft run-out accuracy is indicated below. 
For details about the shaft run-out accuracy, see "III.2.

-out accuracy 
The shaft run-out accuracy is indicated below. 
For details about the shaft run-out accuracy, see "III.2. Mounting a servo motor(P.234)." 
Shaft diameter run-out 
Run-out of the fit surface to the 
shaft center 
Run-out of the flange mounting 
surface to the shaft center 
0.03 mm or less 
0.05 mm or less 
0.06 mm or less

(5) Power connector 
Types of power connectors 
The power connector of each model is as follows.
```

---

## 第 161 頁
**本頁字數:** 863 字

### 內容摘要:
```text
Motor specifications 
147 
Model 
Power connector 
All models other than the followings 
MS 22-22P compatible connector 
αiS 50/3000-D, αiS 50/3000 FAN-D 
αiS 60/3000-D, αiS 60/3000 FAN-D 
MS 24-10P compatible connector

- MS22-22P compatible connector 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
Hirose Electric 
JL10-2E22-22PE 
H/MSD3102A22-22P-D-T

As the power connector, a receptacle connector having a waterproof property by itself (when it is not engaged) is 
used as standard. 
Either a bayonet-type connector or screw-type connector can be connected. 
Strictly speaking, this power connector does not meet the MS standard, but it can be used as a connector compatible 
with the MS-standard round connector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance.
```

---

## 第 161 頁
**本頁字數:** 1134 字

### 內容摘要:
```text
nnector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance. 
Contact the manufacturer of the connector in question.

The following shows the specification, shape, and pin layout of the power connector.

MS24-10P compatible connector 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JL10-2E24-10PE(G)-B

As the power connector, a receptacle connector having a waterproof property by itself (when it is not engaged) is 
used as standard. 
Either a bayonet-type connector or screw-type connector can be connected. 
Strictly speaking, this power connector does not meet the MS standard, but it can be used as a connector compatible 
with the MS-standard round connector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance.

nnector. 
Connecting a plug connector other than those mentioned in this manual may lead to poor waterproof performance. 
Contact the manufacturer of the connector in question.

The following shows the specification, shape, and pin layout of the power connector.
```

---

## 第 162 頁
**本頁字數:** 997 字

### 內容摘要:
```text
(6) Connectors for the brake 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JN2AS04MK3-R

Brake connectors are waterproof in themselves (unengaged). 
The following shows the shape and pin arrangement of the brake connectors. 
Connect the power supply for the brake (24 VDC, 0 V) to BK. The brake is nonpolarized. 
For the connected cables and the connectors on the cable side, see "II.1.3.3. Connectors for the brake(P.186)."

NOTE 
No.4 pin is connected to the brake housing. Use it when you need to connect the shield line for the brake cable.

(7) Signal connectors 
For the specifications, shapes, and pin layouts of the signal connectors, see "I.4. Feedback sensors(P.159)."

(8) Cooling fan connector 
For the specifications, shapes, and pin layouts of the cooling fan connector, see separate chapters, see "I.3.4.

nector 
For the specifications, shapes, and pin layouts of the cooling fan connector, see separate chapters, see "I.3.4. Cooling 
fan(P.156)."
```

---

## 第 164 頁
**本頁字數:** 856 字

### 內容摘要:
```text
150 
3.3.2. 
Connecting a brake 
(1) Brake connectors 
See "I.3.2. Outline drawings(P.117)" for the specifications, shapes, and pin layouts of the brake connectors, 
and see "II.1.3. Connectors on the cable side(P.175)" for the connected cables and the connectors on the cable side.

(2-1) When the brake circuit for servo amplifier is used (recommended)

FANUC SERVO AMPLIFIER αi-D series include a brake circuit. 
For details, refer to ""SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN)."

(2-1) When the brake circuit for servo amplifier is not used

Constitute a brake circuit by reference to the following.

(2-2-1) Connection of the brakes

1. Use 24 VDC as power supply for the brake of the FANUC SERVO MOTOR αi-D series. Power produced by full-
wave rectification after transforming commercial power supply (50 Hz/60 Hz) is also available. 
2.
```

---

## 第 164 頁
**本頁字數:** 746 字

### 內容摘要:
```text
wer produced by full-
wave rectification after transforming commercial power supply (50 Hz/60 Hz) is also available. 
2. Use a power supply separated path from the 24 V power supply for the CNC and amplifier control as the power 
supply for the brake. If the control power supply is also used for the brake, a CNC or amplifier malfunction or 
another danger may occur. It can be shared with peripheral equipment such as relay and solenoid. Be careful of 
changes in voltage due to power supply capacity and power supply voltage fluctuations in load. 
3. For full-wave rectification, transform the secondary side voltage during energization of the brake into 
approximately 29 VAC by taking the voltage drop in the rectifier or cable into account.
```

---

## 第 164 頁
**本頁字數:** 1090 字

### 內容摘要:
```text
energization of the brake into 
approximately 29 VAC by taking the voltage drop in the rectifier or cable into account. In this case, check the 
power supply capacity and power supply voltage fluctuations sufficiently and then make sure the fluctuations in 
the voltage applied to the brake during energization fall within 24 Vrms ± 10%. Use the input switching for the 
primary side of the transformer such as 100-110-120 VAC or 200-220-240 VAC. 
4. Since the brake is an inductive load, the durability of the switch contacts is lowered compared with a resistive 
load. Use a contact with sufficient capacity and confirm the durability of the switch's contact on an actual machine. 
5. If multiple brakes are used, use separate circuits for each brake except for the power supply. 
6.

n actual machine. 
5. If multiple brakes are used, use separate circuits for each brake except for the power supply. 
6. Since the brake coil has no polarity, it does not matter whether the positive or negative of the power supply is 
connected in either direction. 
7. Use a shielded cable as required.
```

---

## 第 165 頁
**本頁字數:** 725 字

### 內容摘要:
```text
Motor specifications 
151 
(2-2-2) Parts for brake circuits

<Normal use (switching frequency of up to a hundred thousand times> 
Product name 
Model No. 
specifications 
Name of 
manufacturer 
FANUC procurement 
Dwg. No. 
Surge absorber 
ERZV10D820 
Varistor voltage 82 V 
Max. allowable circuit voltage 50 
VAC 
Panasonic 
Corporation 
- 
Spark killer 
XEB0471 
0.1 μF / 47 Ω 
Rated voltage 250 VAC 
OKAYA 
ELECTRIC IND. 
CO., LTD. 
- 
Switch 
LY2 
Rated load 
AC110V 10A / DC24V 10A 
OMRON 
Corporation 
- 
Rectifier 
D3SB60 
(Note 1) 
Peak reverse voltage: 600 V 
Output current: 2.3 A (with no fin) 
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD. 
A06B-6050-K112 
The specifications of parts for brake circuits are only reference.
```

---

## 第 165 頁
**本頁字數:** 854 字

### 內容摘要:
```text
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD. 
A06B-6050-K112 
The specifications of parts for brake circuits are only reference. Although there are examples of switching tests of 
approximately a hundred thousand times with a combination listed above, no failure is not guaranteed.

<High-frequency use (switching frequency exceeding a hundred thousand times> 
Name 
Model No. 
specifications 
Name of 
manufacturer 
FANUC procurement 
Dwg. No. 
Surge absorber 
ERZV10D820 
Varistor voltage 82 V 
Max. allowable circuit voltage 50 
VAC 
Panasonic 
Corporation 
- 
Spark killer 
XEB0105 
0.5μF / 10Ω 
Rated voltage 250 VAC 
OKAYA 
ELECTRIC IND. 
CO., LTD. 
- 
Switch 
LY2 
Rated load 
AC110V 10A / DC24V 10A 
OMRON 
Corporation 
- 
Rectifier 
D3SB60 
(Note 1) 
Peak reverse voltage: 600 V 
Output current: 2.3 A (with no fin) 
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD.
```

---

## 第 165 頁
**本頁字數:** 928 字

### 內容摘要:
```text
D3SB60 
(Note 1) 
Peak reverse voltage: 600 V 
Output current: 2.3 A (with no fin) 
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD. 
A06B-6050-K112 
The specifications of parts for brake circuits are only reference. Although there are examples of switching tests of 
approximately two million times with a combination listed above, no failure is not guaranteed.

Confirm the durability of switch's contact on an actual machine according to the required switching frequency. If the 
switch contact in the brake circuit cannot be open, the brake will remain in the released state and the machine may not 
be held.

NOTE 
1. At an ambient temperature of 20°C, the temperature of the rectifier rises to about 60°C when one brake axis is 
used or to about 90°C when two brake axes are used.

erature of the rectifier rises to about 60°C when one brake axis is 
used or to about 90°C when two brake axes are used. Use a radiator fin as required.
```

---

## 第 166 頁
**本頁字數:** 664 字

### 內容摘要:
```text
<Normal use (switching frequency of up to a hundred thousand times> 
Name 
Model No. 
specifications 
Name of 
manufacturer 
FANUC procurement 
Dwg. No. 
Surge absorber 
ERZV20D820 
(Note 1) 
Varistor voltage 82 V 
Max. allowable circuit voltage 50 
VAC 
Panasonic 
Corporation 
- 
Spark killer 
XEB0105 
0.5μF / 10Ω 
Rated voltage 250 VAC 
OKAYA 
ELECTRIC IND. 
CO., LTD. 
- 
Switch 
LY2 
Rated load 
AC110V 10A / DC24V 10A 
OMRON 
Corporation 
- 
Rectifier 
D3SB60 
(Note 2) 
Peak reverse voltage: 600 V 
Output current: 2.3 A (with no fin) 
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD. 
A06B-6050-K112 
The specifications of parts for brake circuits are only reference.
```

---

## 第 166 頁
**本頁字數:** 892 字

### 內容摘要:
```text
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD. 
A06B-6050-K112 
The specifications of parts for brake circuits are only reference. Although there are examples of switching tests of 
approximately a hundred thousand times with a combination listed above, no failure is not guaranteed.

<High-frequency use (switching frequency exceeding a hundred thousand times> 
Name 
Model No. 
specifications 
Name of 
manufacturer 
FANUC procurement 
Dwg. No. 
Surge absorber 
ERZV20D820 
(Note 1) 
Varistor voltage 82 V 
Max. allowable circuit voltage 50 
VAC 
Panasonic 
Corporation 
- 
Spark killer 
XEB0105 
Two in 
parallel 
1.0 μF / 5 Ω (Note 3) 
Rated voltage 250 VAC 
OKAYA 
ELECTRIC IND. 
CO., LTD. 
- 
Switch 
LY2 
Rated load 
AC110V 10A / DC24V 10A 
OMRON 
Corporation 
- 
Rectifier 
D3SB60 
(Note 2) 
Peak reverse voltage: 600 V 
Output current: 2.3 A (with no fin) 
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD.
```

---

## 第 166 頁
**本頁字數:** 587 字

### 內容摘要:
```text
D3SB60 
(Note 2) 
Peak reverse voltage: 600 V 
Output current: 2.3 A (with no fin) 
SHINDENGEN 
ELECTRIC MFG. 
CO., LTD. 
A06B-6050-K112 
The specifications of parts for brake circuits are only reference. Although there are examples of switching tests of 
approximately two million times with a combination listed above, no failure is not guaranteed.

NOTE 
1. The surge absorber capacity is getting increase against that for the 35Nm brake. 
2. Use a radiator fin, etc., and use one brake axis per rectifier. 
3. The specifications indicates when two spark killers are used in parallel.
```

---

## 第 167 頁
**本頁字數:** 786 字

### 內容摘要:
```text
Motor specifications 
153 
(2-2-3) Reducing the amount of brake axis dropping 
When using a motor with a brake, the amount of axis dropping at a power failure or emergency stop condition, or 
when the CNC power supply is turned off during excitation of the motor may become an issue. To operate the brake 
immediately and reduce the amount of axis dropping to a minimum, note the following points:

1. To operate the brake immediately, the switch and relay for controlling on and off must be installed on the DC side 
(at the position shown in the following figure) of the break circuit. 
If the contact is installed on the AC side (between the transformer's secondary side and rectifier), it takes time 
until holding starts because of the current returned to the rectifier diodes. 
2.
```

---

## 第 167 頁
**本頁字數:** 980 字

### 內容摘要:
```text
ry side and rectifier), it takes time 
until holding starts because of the current returned to the rectifier diodes. 
2. To reduce the amount of vertical axis dropping, the switch or relay must be turned off at a power failure as soon 
as possible. To cut off the relay immediately at a power failure, it is effective to take off directly the power supply 
for the driving the relay from the main power supply whenever possible as shown in the following figure. 
3. To prevent the axis from dropping at a moment of an emergency stop condition, use the "Brake control" in the 
servo software. This function enables continuous excitation of the motor for a set time until the motor built-in 
brake operates.

tware. This function enables continuous excitation of the motor for a set time until the motor built-in 
brake operates. For details, refer to ""AC SERVO MOTOR αi-B/αi/βi-B/βi series, LINEAR MOTOR LiS-B/LiS 
series, DD MOTOR DiS-B/DiS series PARAMETER MANUAL" (B-65270EN)."
```

---

## 第 168 頁
**本頁字數:** 892 字

### 內容摘要:
```text
154 
3.3.3. 
Reduced backlash brake 
A reduced backlash brake is a brake used to reduce a small amount of axis dropping that may occur in the event of 
an emergency stop condition or power outage due to the backlash of the built-in brake and motor shaft.

The mechanical and electrical specifications of a reduced backlash brake are the same as the standard brake. The 
external dimensions and mounting dimensions of the motor are also the same as those with the standard brake.

When using a motor with a reduced backlash brake, follow the instructions given below. 
Otherwise, it cannot get the effectiveness in reducing the small amount of axis dropping and it may cause of the 
motor fail.

1. Mount the motor with the shaft facing downward, as shown on the right. Arrange mechanically so that the vertical 
axis drops when the motor is turned counterclockwise relative to the Pulsecoder.
```

---

## 第 168 頁
**本頁字數:** 620 字

### 內容摘要:
```text
ange mechanically so that the vertical 
axis drops when the motor is turned counterclockwise relative to the Pulsecoder. (Turning the motor clockwise 
does not produce any reduction effect.) 
2. If the gravity load torque is great and there is little leeway in the brake holding torque, the reduction effect 
becomes weaker, resulting in an increase in the small amount of axis dropping. It is recommended to use the 
motor with not more than 70% of the brake holding torque. 
3. If the gravity axis pulling up at emergency stop condition function is used at the same time, no backlash reduction 
effect can be obtained.
```

---

## 第 169 頁
**本頁字數:** 819 字

### 內容摘要:
```text
Motor specifications 
155 
3.3.4. 
Cautions on use 
When using a motor with built-in brake, follow the instructions given below. Otherwise it may cause a failure and 
impossible to hold the machine. 
1. The built-in brake is designed for holding. Do not use the brake for braking. 
2. Do not operate the motor without the brake released. 
3. Do not apply the command to rotate the motor until the brake has been released completely. 
4. Release the brake after the motor excitation is turned on. Hold the brake before the motor excitation is turned off. 
5. Do not use the brake as a support for stopping, with the motor placed in the excitation state. 
6. Make sure that the motor surface does not get wet with the cutting fluid, etc. For details, see "III.3.2. Usage 
considering environmental resistance(P.244)." 
7.
```

---

## 第 169 頁
**本頁字數:** 899 字

### 內容摘要:
```text
get wet with the cutting fluid, etc. For details, see "III.3.2. Usage 
considering environmental resistance(P.244)." 
7. The overall length of a model with a built-in brake, such as the αiF 40-D, is much longer than that of the model 
with no built-in brake. Be careful not to apply excessive force to the opposite side of the mounting flange or to 
apply excessive acceleration to the entire motor. 
8. With the following models, which have iron shafts, the shaft gets slightly magnetized when releasing the brake. 
αiS 8/3000-D, αiS 8/3000HV-D 
αiS 12/2000-D 
αiS 12/3000-D, αiS 12/3000HV-D 
αiS 22/2000-D, αiS 22/2000HV-D 
αiS 22/3000-D, αiS 22/3000HV-D 
αiS 30/3000-D, αiS 30/3000HV-D 
αiS 40/2500-D, αiS 40/2500HV-D 
For connection with a coupling 
The coupling attenuates the flux density, so the machine is slightly affected by the magnetized shaft. Check it on 
an actual machine to be sure.
```

---

## 第 169 頁
**本頁字數:** 537 字

### 內容摘要:
```text
he flux density, so the machine is slightly affected by the magnetized shaft. Check it on 
an actual machine to be sure. 
For connection with gears  
The machine is affected more than for connection with a coupling. Carefully check with an actual machine that the 
entry of magnetized foreign material such as cutting chips adversely affect gears.

On the machine, install a stop device for securing safety. 
The brake built into the servo motor is not a stop device for securing safety. The machine may not be held if a failure 
occurs.
```

---

## 第 170 頁
**本頁字數:** 680 字

### 內容摘要:
```text
156 
3.4. 
Cooling fan 
αiS 50 FAN-D, αiS 60 FAN-D, αiF 40 FAN-D (including HV) have a cooling fan installed. This subsection describes 
these cooling fans. 
3.4.1. 
Cooling fan specifications 
The specifications of the cooling fan supplied with each motor are listed below.

Model 
αiS 50/3000 FAN-D, αiS 60/3000 FAN-D, αiF 40/3000 FAN-D (including HV) 
Input voltage range 
Single-phase 200-250 VAC 
Rated voltage 
Single-phase 200 
VAC 
Single-phase 230 
VAC 
Single-phase 200 
VAC 
Single-phase 230 
VAC 
Frequency 
50Hz 
60Hz 
Rated input 
37W±10% 
53W±10% 
31W±10% 
44W±10% 
Rated current 
0.220A±10% 
0.270A±10% 
0.175A±10% 
0.220A±10% 
Protection class 
(IEC60034-5) 
IP65
```

---

## 第 171 頁
**本頁字數:** 1157 字

### 內容摘要:
```text
Motor specifications 
157 
3.4.2. 
Connecting a cooling fan 
(1) In case that other electronics devices are in parallel with fan 
Refer the below connecting example in case that electronics devices other than cooling fan connect in parallel with 
the breaker for cooling fan or magnetic contactor.

NOTE 
Such as when other electronic device connect in parallel with the cooling fan, if there is a need to reduce the impact of 
surge voltage which is generated at power supply when open and close the magnetic contactor, use a spark killer.

(2) Cooling fan circuit 
The connector pin layout and connection diagram for the cooling fan are shown below. 
For the connected cables and the connectors on the cable side, see "II.1.3.

iagram for the cooling fan are shown below. 
For the connected cables and the connectors on the cable side, see "II.1.3. Connectors on the cable side(P.175)."

αiS 50 FAN-D, αiS 60 FAN-D, αiF 40 FAN-D (including HV) 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JN2AS04MK2X-R

The connectors are waterproof in themselves (unengaged). 
The shape and pin layout of the connector are shown below.
```

---

## 第 172 頁
**本頁字數:** 665 字

### 內容摘要:
```text
158 
An example of circuit diagram that uses a spark killer is shown below.

(3) Cooling fan circuit parts 
Constitute a cooling fan circuit by referring to the parts shown in the below.

Applicable spark killer (recommend) 
Model No. 
Name of manufacturer 
specifications 
XEB0473 
OKAYA ELECTRIC IND. CO., 
LTD. 
0.3 μF / 47 Ω 
Rated voltage 250 V 
* 
Up to four cooling fan can be connected in parallel with one spark killer.

(4) Cooling fan protection circuit 
The fan motor inside the cooling fan includes a protection circuit based on a thermal protector. 
A thermal protector operates when the temperature of the winding inside the fan motor rises to 140°C.
```

---

## 第 173 頁
**本頁字數:** 766 字

### 內容摘要:
```text
Feedback sensors 
159 
4. 
Feedback sensors 
All FANUC αi-D series servo motors contain a Pulsecoder (optical encoder) as a feedback detector that detects 
position and speed. 
Separate type Pulsecoder are also available for detecting a position by attaching directly to a ball screw or machine. 
4.1. 
Pulsecoder 
All FANUC SERVO MOTOR αi-D series contain a Pulsecoder (optical encoder). The Pulsecoder outputs position 
information and an alarm signal. 
The outline drawing of Pulsecoder is not given in this section because it is contained in a motor. 
Refer to "I.3.2. outline drawing(P.117)." 
4.1.1. 
Types of Pulsecoders and designation 
Pulsecoders are defined together with motors. Refer to "I.2. Ordering specification numbers(P.6)" for how to define them.
```

---

## 第 173 頁
**本頁字數:** 1103 字

### 內容摘要:
```text
ulsecoders are defined together with motors. Refer to "I.2. Ordering specification numbers(P.6)" for how to define them. 
The following table lists the types of Pulsecoders.

Applicable motor 
Resolution [div/rev] 
Remarks 
αiS 0.2-D to αiS 0.3-D 
500,000 
Standard, battery-less (note 1) 
αiS 0.5-D to αiS 1.5-D (including HV) 
1,000,000 
Standard, battery-less (note 1) 
αiS 2-D to αiS 60-D (including HV) 
αiF 1-D to αiF 40-D (including HV) 
4,000,000 
Standard (αiA4000-D) (note 2) 
Battery-less (αiA4000BL-D) (note 2) 
αiS 2-D to αiS 60-D (including HV) 
αiF 1-D to αiF 40-D (including HV) 
32,000,000 
High resolution (αiA32000-D) (note 2)

NOTE 
1. Maintenance by a motor as it is installed in a motor. 
2. Separate maintenance is possible for the Pulsecoder as it can be detached from a motor. 
3.

is installed in a motor. 
2. Separate maintenance is possible for the Pulsecoder as it can be detached from a motor. 
3. The same Pulsecoder as 200-V motor is used for 400-V motors.

Pulsecoders (battery-less) can retain their positions with no battery connected even after the CNC is turned off.
```

---

## 第 174 頁
**本頁字數:** 674 字

### 內容摘要:
```text
160 
4.1.2. 
Connecting Pulsecoder 
Connectors 
Manufacturer 
Manufacturer specification 
Japan Aviation Electronics Industry 
JN2AS10UL1-R 
Hirose Electric 
HR34B-12WR-10PD3 series

The connector of the αi-D series Pulsecoder is waterproof when engaged with the cable side connector. (When it 
comes to the motor alone, the connector is waterproof when the cap mounted at shipment is fit in the connector.) 
If it is not completely engaged or liquid infiltrates into the connector-engaged part through the cable, the liquid 
infiltrates into the Pulsecoder, which may cause an alarm. 
The signals of the αi-D series Pulsecoder are arranged as follows:

Signal name 
Pin No.
```

---

## 第 174 頁
**本頁字數:** 944 字

### 內容摘要:
```text
der, which may cause an alarm. 
The signals of the αi-D series Pulsecoder are arranged as follows:

Signal name 
Pin No. 
RD 
6 
*RD 
5 
+5V 
8,9 
0V 
7,10 
FG 
3 
+6V 
(Not required for battery-less) 
4

Do not wire pins not specified.

Connector kits 
For information on connectors and crimping fixture required for creating a feedback cable, see "II.1.3.1. Connectors for 
signals (for all αi-D series models)(P.176)."

If the motor is mounted on the movable parts, or a flexible tube or conduit hose is used for the connector, excessive 
force may be applied to the connector.

e parts, or a flexible tube or conduit hose is used for the connector, excessive 
force may be applied to the connector. In this case, fix the feedback cable to prevent the connector from being 
damaged.

Connecting Pulsecoder to an amplifier 
For the connection cable for Pulsecoder and an amplifier, see "SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-
65552EN).
```

---

## 第 175 頁
**本頁字數:** 920 字

### 內容摘要:
```text
Feedback sensors 
161 
4.1.3. 
Pulsecoder (standard) 
Pulsecoder (standard) position detection function is backed up by battery even after the CNC is turned off. So, when 
the CNC is next turned on, the operator does not have to perform reference position return. 
For backup, however, a battery unit must be installed in the CNC or servo amplifier. If a low-battery indication 
appears on the CNC, replace the battery as soon as possible. 
For any servo motor, the function is backed up for about 10 minutes by a backup capacitor contained in the 
Pulsecoder when the battery is removed. In the backup status, the battery can be replaced when turn the servo 
amplifier off. The operator does not also have to perform reference position return after replacing the feedback cable 
or servo amplifier.

perator does not also have to perform reference position return after replacing the feedback cable 
or servo amplifier.
```

---

## 第 176 頁
**本頁字數:** 879 字

### 內容摘要:
```text
162 
4.1.4. 
Pulsecoder (battery-less) 
Pulsecoders (battery-less) can retain their positions with no battery connected even after the CNC is turned off. 
Operating a servo motor with a Pulsecoder (battery-less) requires compatible CNC system software and servo control 
software. When using unsupported CNC system software and servo control software, α Pulsecoder software 
disconnection alarm will occur and it cannot be operated.

CNC system software, servo control software 
Servo motors with Pulsecoder (battery-less) can be operated with CNC system software and servo control software 
supporting FANUC SERVO MOTOR αi-D series operation. 
For details, refer to "I.1.3. Supported CNC system software, servo control software(P.5)."

Setting parameters 
Set standard parameters and detector-related parameters for the servo motor in the same setting as Pulsecoder 
(standard).
```

---

## 第 176 頁
**本頁字數:** 838 字

### 內容摘要:
```text
t standard parameters and detector-related parameters for the servo motor in the same setting as Pulsecoder 
(standard). For details, see "Setting parameters for a servo motor" of "AC SERVO MOTOR αi-B/αi/βi-B/βi series, 
LINEAR MOTOR LiS-B/LiS series, DD MOTOR DiS-B/DiS series PARAMETER MANUAL" (B-65270EN).

Replacing the Pulsecoder 
The procedure for replacing a Pulsecoder (battery-less) is the same as the procedure for Pulsecoder (standard). 
For details, see "SERVO MOTOR αi-D series, SPINDLE MOTOR αi-D series, SERVO AMPLIFIER αi-D series 
MAINTENANCE MANUAL" (B-65555EN). 
When a Pulsecoder is replaced for a servo motor with a Pulsecoder (battery-less), reference position return is 
required same as a standard Pulsecoder. After a standard Pulsecoder is replaced, BZAL is issued as well as a 
reference position return request.
```

---

## 第 176 頁
**本頁字數:** 580 字

### 內容摘要:
```text
ard Pulsecoder. After a standard Pulsecoder is replaced, BZAL is issued as well as a 
reference position return request. But when a Pulsecoder (battery-less) is replaced, only a reference position return 
request is issued and no BZAL is issued.

Restriction on use 
When a Pulsecoder (battery-less) is used as a linear axis or rotary axis B type, the movable range is ±2000 rev from 
the machine coordinate origin. 
If the above range is exceeded, DS0300 (reference position request) and PW0000 (power-off request) is issued 
frequently and reference position return is required.
```

---

## 第 177 頁
**本頁字數:** 445 字

### 內容摘要:
```text
Feedback sensors 
163 
4.2. 
Separate Pulsecoder 
For detecting a position by attaching a detector directly to a ball screw or a machine, use a separate Pulsecoder. 
4.2.1. 
Separate Pulsecoder type and designation 
The following separate Pulsecoder is available.

Separate Pulsecoder 
name 
Resolution 
Allowable 
maximum 
speed 
Absolute/ 
Incremental 
Designation method 
αiA4000S 
4,000,000 /rev 
6,000min-1 
Absolute 
A860-2052-T321 
4.2.2.
```

---

## 第 177 頁
**本頁字數:** 1115 字

### 內容摘要:
```text
peed 
Absolute/ 
Incremental 
Designation method 
αiA4000S 
4,000,000 /rev 
6,000min-1 
Absolute 
A860-2052-T321 
4.2.2. 
Separate Pulsecoder specifications 
Specifications of Pulsecoder αiA4000S 
Item 
specifications 
Power supply voltage 
5 [V] ± 5% 
Current consumption 
0.2 [A] or less 
Working temperature range 
0 to +60 [°C] 
Resolution 
4,000,000 [/rev] 
Maximum rotation speed 
6,000 [min-1] 
Input shaft moment of inertia 
9.8 × 10-3 [kgꞏm2] or less 
Input shaft startup torque 
Up to 0.098 [Nꞏm] 
Input shaft 
allowable load 
Radial load 
98 [N] 
Axial load 
49 [N] 
Shaft diameter run-out 
0.02 × 10-3[m] 
Structure 
Dust-proof, drip-proof (IP55 or equivalent: when water-proof connector is 
fitted) 
Vibration resistance acceleration 
5 [G](50\~2,000[Hz]) 
Weight 
Approx.

valent: when water-proof connector is 
fitted) 
Vibration resistance acceleration 
5 [G](50\~2,000[Hz]) 
Weight 
Approx. 0.6 [kg] 
* 
For the positional relationship between the shaft keyway and the origin in the rotation direction of the separate 
Pulsecoder shaft, see "I.4.2.5. Notes on using the separate Pulsecoder(P.166)."
```

---

## 第 178 頁
**本頁字數:** 424 字

### 內容摘要:
```text
164 
4.2.3. 
Connecting a separate Pulsecoder 
For the connection diagram for separate Pulsecoders, refer to the relevant CNC connection manual.

Connectors 
The connector of the αiA4000S series separate Pulsecoder is waterproof when engaged with the cable connector.

Connector pin layout 
The layout of connector pins is shown below.

Signal name 
Pin No. 
SD 
2 
*SD 
1 
REQ 
6 
*REQ 
5 
+5V 
8,9 
0V 
7,10 
FG 
3 
+6V 
4
```

---

## 第 179 頁
**本頁字數:** 179 字

### 內容摘要:
```text
Feedback sensors 
165 
4.2.4. 
Outline drawings of separate Pulsecoder

NOTE 
The shaft shape (including a keyway), flange-side fit, and mounting hole are compatible with αA1000S.
```

---

## 第 180 頁
**本頁字數:** 799 字

### 內容摘要:
```text
166 
4.2.5. 
Notes on using the separate Pulsecoder 
Pay attention to the following items when using a separate Pulsecoder. 
 
When using the separate Pulsecoder, increase the machine rigidity between the servo motor and the Pulsecoder 
to minimize backlash. If the machine rigidity is low or the backlash is large, vibration, overshoot, or other problems 
are likely to occur. 
 
When a separate Pulsecoder is used, the influence of gear, belt pitch error, or table inclination decreases and the 
positioning accuracy increases, but the smoothness may decrease if the machine rigidity is low or the backlash is 
large between the servo motor and the separate Pulsecoder. 
 
It is necessary to use the built-in Pulsecoder with a resolution equal to or finer than that of the separate 
Pulsecoder.
```

---

## 第 180 頁
**本頁字數:** 575 字

### 內容摘要:
```text
t is necessary to use the built-in Pulsecoder with a resolution equal to or finer than that of the separate 
Pulsecoder. 
 
To connect the separate Pulsecoder to the CNC, connect only the signals described in the CNC connection 
manual. When the other signal is connected, the unit may occur malfunction. 
 
When the key way of the shaft is located at the position of the connector, which is regarded as the position of 0°, 
the origin of the separate Pulsecoder is located at 0°±10°. (See the figure below.)

Positional relationship between the origin and the shaft keyway
```

---

## 第 183 頁
**本頁字數:** 780 字

### 內容摘要:
```text
System configuration 
169 
1. 
System configuration

1.1. 
Connecting a servo motor 
For the FANUC SERVO MOTOR αi-D series, connect the power line of the motor and the signal line of a Pulsecoder 
to an FANUC servo amplifier. When the motor has a built-in brake or cooling fan as an option, connect the built-in 
brake or cooling fan to the specified power supply.

If a motor is not connected to ground through the machine (cabinet) in which the motor is installed, connect the motor 
grounding point and the amplifier grounding point to absorb noise immunity. 
In this case, use a wire with a thickness of at least 1.25 mm2, other than the GND conductor in the power line. Keep the 
wire as far from the power line as possible.

the 
wire as far from the power line as possible.
```

---

## 第 184 頁
**本頁字數:** 665 字

### 內容摘要:
```text
170 
Connecting the power line 
For the pin layout of the power connector on the servo motor side or the layout of the power terminals, see "I.3.2. 
Outline drawings(P.117)." 
For details of the connector of a cable connected to the servo motor, see "II.1.3. Connectors on the cable side(P.175)." 
For the selection of power lines and for the connectors and terminal shapes to connect to servo amplifiers, see 
"SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN).

Connecting the signal line 
For details of the signal connector on a Pulsecoder, see "I.4. Feedback sensors(P.159)." 
For details of the connector of a cable connected to a Pulsecoder, see "II.1.3.
```

---

## 第 184 頁
**本頁字數:** 1031 字

### 內容摘要:
```text
er, see "I.4. Feedback sensors(P.159)." 
For details of the connector of a cable connected to a Pulsecoder, see "II.1.3. Connectors on the cable side(P.175)." 
For the selection of signal lines and for the connectors to connect to servo amplifiers, see "SERVO AMPLIFIER αi-D 
series DESCRIPTIONS" (B-65552EN).

Connecting a built-in brake 
For connectors for the brake on built-in brake side, see "I.3.2. Outline drawings(P.117)." 
For how to connect power supply, see "I.3.3. Built-in brake(P.149)." 
For the connector of a cable connected to a built-in brake, see "II.1.3. Connectors on the cable side(P.175)."

Connecting a cooling fan 
For the cooling fan connector on the cooling fan side, the type of power supply for driving the cooling fan, and power 
cabling, see "I.3.4. Cooling fan(P.156)." 
For the connector of a cable connected to a cooling fan, see "II.1.3.

power 
cabling, see "I.3.4. Cooling fan(P.156)." 
For the connector of a cable connected to a cooling fan, see "II.1.3. Connectors on the cable side(P.175)."
```

---

## 第 185 頁
**本頁字數:** 610 字

### 內容摘要:
```text
System configuration 
171 
1.2. 
Applicable amplifiers 
The FANUC SERVO MOTOR αi-D series can be driven using FANUC Servo Amplifier αiSV-D series, αiSVP-D 
series, αiPSV-D series, or αiPSVSP-D series. 
For an order specification number of the servo amplifier, see "SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-
65552EN).

Combination of servo motor and servo amplifier (200V)

αiSV 20-D 
αiPSV 20-D 
- 
▲ 
○

αiSV 20/20-D 
αiPSV 20/20-D 
αiPSVSP 20/20-7.5-D 
αiPSVSP 20/20-11-D 
L axis 
▲ 
○

αiSV 40/40-D 
αiPSV 40/40-D 
αiPSVSP 40/40-18-D 
L axis

αiSV 80/80-D 
αiPSVSP 80/80-18-D 
αiPSVSP 80/80-26-D 
L axis
```

---

## 第 186 頁
**本頁字數:** 275 字

### 內容摘要:
```text
αiPSVSP 80/80/160-26-D 
L axis

Note) Each symbol is as described below. 
○ : Standard combination. 
▲ : To combine this motor, the motor control parameter must be changed. 
If you wish to use this combination, contact FANUC. 
Invalid parameter settings may damage the motor.
```

---

## 第 188 頁
**本頁字數:** 881 字

### 內容摘要:
```text
αiPSVSP 40/40/80-26HV-D 
L axis

Note) Each symbol is as described below. 
○ : Standard combination. 
▲ : To combine this motor, the motor control parameter must be changed. 
If you wish to use this combination, contact FANUC. 
Invalid parameter settings may damage the motor.

1. Read the "coefficients for dynamic brake calculation" to confirm whether the dynamic brake stop distance fits the 
desired stop distance. For the calculation and details of the dynamic brake stop distance, see "II.2.2.7. Calculating 
the dynamic brake stop distance(P.213)."  
2. For all the motors, it is recommended to apply the quick stop function as a function to shorten the stop distance in 
the event of an emergency stop or a power failure. Refer to ""AC SERVO MOTOR αi-B/αi/βi-B/βi series, LINEAR 
MOTOR LiS-B/LiS series, DD MOTOR DiS-B/DiS series PARAMETER MANUAL" (B-65270EN)" for details.
```

---

## 第 188 頁
**本頁字數:** 918 字

### 內容摘要:
```text
αi/βi-B/βi series, LINEAR 
MOTOR LiS-B/LiS series, DD MOTOR DiS-B/DiS series PARAMETER MANUAL" (B-65270EN)" for details. To 
ensure the quick stop function works in the event of a power failure, maintain the control power supply (24 VDC) 
for the CNC and servo amplifier by using an uninterruptible power supply (UPS) for example. 
3. If an alarm occurs, the quick stop function does not operate effectively and the stop distance will not be shortened. 
4. If you wish to use the quick stop function, it should be confirmed with an actual machine that the stop distance is 
shortened at an emergency stop or power failure.

1. If a motor is used in a combination other than those listed above, it may be damaged. 
2. For servo amplifiers, see "SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN).

listed above, it may be damaged. 
2. For servo amplifiers, see "SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN).
```

---

## 第 190 頁
**本頁字數:** 515 字

### 內容摘要:
```text
176 
1.3.1. 
Connectors for signals (for all αi-D series models) 
As connectors for signals, the same small dedicated connector is used for all the FANUC SERVO MOTOR αi-D 
series models. 
The connector is waterproof when engaged with the motor connector. There are two types of connector to connect 
the cable: crimp type and solder type. For a crimp type connector, a dedicated crimping tool of its manufacturer must 
be used. 
The diameter of the cable used is restricted considering cable clamp and voltage drop.
```

---

## 第 190 頁
**本頁字數:** 871 字

### 內容摘要:
```text
its manufacturer must 
be used. 
The diameter of the cable used is restricted considering cable clamp and voltage drop. 
The connectors for signals do not have to conform to IEC60034.

Crimp type connector (Japan Aviation Electronics Industry)

For signal 
Connector kits 
(FANUC 
specification) 
Straight type 
A06B-6114-K204#S 
Right angle type 
A06B-6114-K204#E 
* 
The connector kit of the FANUC specification includes the Japan Aviation Electronics 
Industry-made connectors mentioned below (with two types of bushings for applicable cable 
diameters φ5.7 to φ7.3 and φ6.5 to φ8.0) and contacts (individual terminals). 
Contact 
specifications 
Straight type 
JN2DS10SL1-R (Compatible cable O.D. φ5.7 to φ7.3) 
JN2DS10SL2-R (Compatible cable O.D. φ6.5 to φ8.0) 
Right angle type 
JN2FS10SL1-R (Compatible cable O.D. φ5.7 to φ7.3) 
JN2FS10SL2-R (Compatible cable O.D.
```

---

## 第 190 頁
**本頁字數:** 580 字

### 內容摘要:
```text
φ6.5 to φ8.0) 
Right angle type 
JN2FS10SL1-R (Compatible cable O.D. φ5.7 to φ7.3) 
JN2FS10SL2-R (Compatible cable O.D. φ6.5 to φ8.0) 
Contact 
specifications 
Individual 
JN1-22-22S-PKG100 (100 pieces) 
Reel 
JN1-22-22S-10000 (10,000 pieces) 
Insulation external 
diameter 
φ1.5 or less 
Used wire

0V, 5V 
6V 
RD, *RD 
Cable length: 20 m or 
less 
0.3 mm2 x 2 
0.3 mm2 
0.18 mm2 or more 
Twisted pair 
Cable length of 50 m 
or less 
Use the following wire strand. 
(When purchasing, please notify the FANUC specification below to a 
manufacturer.) 
Manufacturer: Proterial, Ltd.
```

---

## 第 190 頁
**本頁字數:** 1026 字

### 內容摘要:
```text
rand. 
(When purchasing, please notify the FANUC specification below to a 
manufacturer.) 
Manufacturer: Proterial, Ltd. 
FANUC specification: A66L-0001-0851 
Tool for crimping 
terminal 
Handy crimping 
tool 
AWG 
#21 (0.5mm2: 20/0.18) 
#23 (0.3mm2) 
#25 (0.18mm2) 
Japan Aviation 
Electronics Industry 
specification 
CT150-2-JN1-E 
FANUC 
A06B-6114-
K201#JN1E 
AWG 
#20 (0.5mm2: 104/0.08) 
#21 (0.5mm2: 20/0.18) 
#25 (0.18mm2) 
Japan Aviation 
Electronics Industry 
specification 
CT150-2-JN1-D 
FANUC 
A06B-6114-
K201#JN1D 
Automatic crimping 
tool 
Main unit 
CP215-5B 
Applicator 
3502-JN1-2C 
Tool for pulling 
terminal out 
Japan Aviation 
Electronics Industry 
specification 
ET-JN1 
FANUC 
A06B-6114-K201#JN1R

Solder type connector (Japan Aviation Electronics Industry)

For signal 
Contac

ion 
ET-JN1 
FANUC 
A06B-6114-K201#JN1R

Solder type connector (Japan Aviation Electronics Industry)

For signal 
Contact 
specifications 
Individual (100 
pieces) 
JN1-22-22F-PKG100 
Individual (10 pieces) 
JN1-22-22F-PKG10
```

---

## 第 191 頁
**本頁字數:** 696 字

### 內容摘要:
```text
For signal 
Compatible cable 
AWG #20 or less (Insulation external diameter φ1.5 mm or less) 
* 
Connectors of this type use contacts that can be soldered. The other parts of this type are the same as those of 
the crimp type (Japan Aviation Electronics Industry).

Crimp type connector (Hirose Electric)

For signal 
Contact 
specifications 
Straight type 
HR34B-12WPD-10SC (Compatible cable O.D. φ5.7 to φ7.3) 
HR34B-12WPE-10SC (Compatible cable O.D. φ6.5 to φ8.0) 
(HR34B-12WPK-10SC (Compatible cable O.D. φ8.0 to φ9.0)) 
Right angle type 
HR34B-12WLPD-10SC (Compatible cable O.D. φ5.7 to φ7.3) 
HR34B-12WLPE-10SC (Compatible cable O.D. φ6.5 to φ8.0) 
(HR34B-12WLPK-10SC (Compatible cable O.D.
```

---

## 第 191 頁
**本頁字數:** 800 字

### 內容摘要:
```text
le O.D. φ5.7 to φ7.3) 
HR34B-12WLPE-10SC (Compatible cable O.D. φ6.5 to φ8.0) 
(HR34B-12WLPK-10SC (Compatible cable O.D. φ8.0 to φ9.0)) 
Contact 
specifications 
Loose piece contact 
HR34B-SC1-111 
Strip contact 
HR34B-SC1-211 
Compatible cable 
AWG #20\~#25 
Insulation external 
diameter 
φ1.34 or less 
Used wire

0V, 5V 
6V 
RD, *RD 
Cable length: 20 m or 
less 
0.3 mm2x2 
0.3 mm2 
0.18mm2 or more 
Twisted pair 
Tool for crimping 
terminal 
Handy crimping tool (AWG#20, 23, 25) 
HT304/HR34B-1 
Automatic crimping 
tool 
Main unit 
CM-105C 
(applicable terminal 
HR34B-SC1-211) 
Applicator 
AP105-HR34B-1 
Tool for pulling 
terminal out 
RP6-SC-TP 
* 
All specification numbers are Hirose Electric's specification

The internal structure of crimped connectors is different between Hirose Electri
```

---

## 第 191 頁
**本頁字數:** 872 字

### 內容摘要:
```text
rs are Hirose Electric's specification

The internal structure of crimped connectors is different between Hirose Electric and Japan Aviation Electronics 
Industry, and crimping tool and contact are not compatible each other. When assembling connectors, make sure to use 
the contact and the crimping tool of the same manufacturer as the connector.

Solder type connector (Hirose Electric)

For signal 
Connector kits 
(FANUC 
specification) 
Straight type 
A06B-6114-K205#S 
Right angle type 
A06B-6114-K205#E 
* 
With the FANUC specifications, the following connector by Hirose Electric, (with two types of 
bushings and endnuts: for φ5.7 to φ7.3 and for φ6.5 to φ8.0) are included. 
Contact 
specifications 
Straight type 
HR34B-12WPD-10S (Compatible cable O.D. φ5.7 to φ7.3) 
HR34B-12WPE-10S (Compatible cable O.D. φ6.5 to φ8.0) 
(HR34B-12WPK-10S (Compatible cable O.D.
```

---

## 第 191 頁
**本頁字數:** 606 字

### 內容摘要:
```text
cable O.D. φ5.7 to φ7.3) 
HR34B-12WPE-10S (Compatible cable O.D. φ6.5 to φ8.0) 
(HR34B-12WPK-10S (Compatible cable O.D. φ8.0 to φ9.0)) 
Right angle type 
HR34B-12WLPD-10S (Compatible cable O.D. φ5.7 to φ7.3) 
HR34B-12WLPE-10S (Compatible cable O.D. φ6.5 to φ8.0) 
(HR34B-12WLPK-10S (Compatible cable O.D. φ8.0 to φ9.0)) 
Compatible cable 
AWG #20 or less (φ0.8 mm or less) 
Used wire

0V, 5V 
6V 
RD, *RD 
Cable length: 20 m or 
less 
0.3 mm2x2 
0.3 mm2 
0.18 mm2 or more 
Twisted pair 
* 
The outside dimensions of the solder type connector when engaged are the same as those of the crimp type 
connector.
```

---

## 第 192 頁
**本頁字數:** 648 字

### 內容摘要:
```text
178 
1. When you prepare a cable on your own, the total resistance of 5 V and 0 V must be less than or equal to 2 Ω. 
2. The motor-side plug connector accepts a wire whose diameter is 0.5 mm2 (wire construction: 20/0.18 or 104/0.08; 
sheath outer diameter: φ1.5 or less) and a cable whose sheath diameter is φ5.7 to φ8.0. When using a thicker 
wire or cable, take measures described below.

The outside dimensions of each type of connector when engaged are shown below: 
Outside dimensions of Japan Aviation Electronics Industry's crimp type and solder type 
connectors

Outside dimensions of Hirose Electric's crimp type and solder type connectors
```

---

## 第 193 頁
**本頁字數:** 998 字

### 內容摘要:
```text
System configuration 
179 
Procedure for engaging feedback cable connectors 
Engage the feedback cable connectors according to the procedure described below, and check that they are 
engaged securely.

1. Checking the mating surfaces and the key direction 
Check that the mating surfaces are free from any substance such as foreign particles or oil.

2. Engaging the connectors 
Hold the connector at the position shown in the figure, and insert it straightforward until it snaps into place.

3. Checking the engaged status 
 
Check that the arrow on the connector is positioned at the center as shown in the figure below.

g the engaged status 
 
Check that the arrow on the connector is positioned at the center as shown in the figure below. 
If the arrow is not at the center, turn the coupling nut by hand so that the arrow is at the correct position.

 
Hold the connector at the position shown in the figure below, and check that the connector does not come 
off when it is pulled lightly.
```

---

## 第 194 頁
**本頁字數:** 844 字

### 內容摘要:
```text
180 
1.3.2. 
Power connectors 
(1) Connectors for power (Group A) 
Dedicated connectors which are TUV approved are available as the connector for power for group A. 
The following subsection describes the specifications as a connector kit. These connectors are waterproof when 
engaged. 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp. Also note that there are restrictions.

Power 
connector kit specifications 
(Including the contact) 
A06B-6114-K270#ED (FANUC specification) 
Contact specifications 
(Not including the contact) 
JN14FH04SJ2-F (Japan Aviation Electronics Industry 
specification) 
Contact specifications 
JN-18S-C1B-A1-100 (Japan Aviation Electronics 
Industry specification) 
Applicable wire size 
AWG#20～18 
Insulation external diameter 
φ1.6 to φ1.8 
Compatible cable O.D.
```

---

## 第 194 頁
**本頁字數:** 883 字

### 內容摘要:
```text
ustry specification) 
Applicable wire size 
AWG#20～18 
Insulation external diameter 
φ1.6 to φ1.8 
Compatible cable O.D. 
φ6.6 to φ7 
Tool for crimping terminal (Caution 2) 
C7751-CT170-14-JN11 (Japan Aviation Electronics 
Industry specification) 
A06B-6114-K271 (FANUC specification)

1. No straight type power connectors are available. 
2. To connect the cable, a dedicated crimping tool must be used. 
3. The contacts are of the type which crimps the covering in addition to the wire. Follow the dimension of the 
insulation part listed above. However, insulation of a diameter outside the above range may be connected 
depending on the wire or tool. For details, contact the connector manufacturer. 
4. No tool for pulling terminal out is used. 
(2) Connectors for power (Group B) 
Dedicated connectors which are TUV approved are available as the connector for power for Group B.
```

---

## 第 194 頁
**本頁字數:** 1059 字

### 內容摘要:
```text
s for power (Group B) 
Dedicated connectors which are TUV approved are available as the connector for power for Group B. 
The following subsection describes the specifications as a connector kit. The connectors are waterproof in 
themselves (unengaged). 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp. Also note that there are restrictions.

Power 
connector kit specifications 
(Including the contact) 
Straight type 
2320297-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K260#S (FANUC specification) 
Right angle type 
2326768-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K260#E2 (FANUC specification) 
Applicable wire size (Caution 1) 
AWG#20 to 17 
Insulation external diameter 
φ1.85 to φ2.30 
Compatible cable O.D.

on) 
Applicable wire size (Caution 1) 
AWG#20 to 17 
Insulation external diameter 
φ1.85 to φ2.30 
Compatible cable O.D. 
φ9.1 to φ9.8 
Tool for crimping terminal (Caution 2) 
2255334-1 (Tyco Electronics Japan GK specification) 
A06B-6114-K264#C (FANUC specification)
```

---

## 第 195 頁
**本頁字數:** 847 字

### 內容摘要:
```text
System configuration 
181 
1. When fastened together with a shielded wire, the compatible cable size is 0.5 to 0.75 mm2 (AWG20 to 18). 
Besides, the total area of the wire conductor and shield wire need to be 1.05 mm2 or less. 
2. To connect the cable, a dedicated crimping tool must be used. 
3. The contacts are of the type which crimps the covering in addition to the wire. Follow the dimension of the 
insulation part listed above. However, insulation of a diameter outside the above range may be connected 
depending on the wire or tool. For details, contact the connector manufacturer. 
4. No tool for pulling terminal out is used.

(3) Connectors for power (Group C) 
Dedicated connectors which are TUV approved are available as the connector for power for group C. 
The following subsection describes the specifications as a connector kit.
```

---

## 第 195 頁
**本頁字數:** 800 字

### 內容摘要:
```text
lable as the connector for power for group C. 
The following subsection describes the specifications as a connector kit. The connectors are waterproof in 
themselves (unengaged). 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp. Also note that there are restrictions.

Power 
connector kit specifications 
(Including the contact) 
Straight type 
(standard) 
2363934-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K222#S (FANUC specification) 
Right angle type 
2314083-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K222#E (FANUC specification) 
Applicable wire size (Caution 1) 
AWG#18\~16 
Outer diameter of sheath of wire (CAUTION 2) 
φ1.8 to φ2.8 
Compatible cable outer diameter (Caution 3) 
φ9.2 to φ11.4 
Tool for crimping termi
```

---

## 第 195 頁
**本頁字數:** 866 字

### 內容摘要:
```text
h of wire (CAUTION 2) 
φ1.8 to φ2.8 
Compatible cable outer diameter (Caution 3) 
φ9.2 to φ11.4 
Tool for crimping terminal (Caution 4) 
2255334-1 (Tyco Electronics Japan GK specification) 
A06B-6114-K264#C (FANUC specification)

1. The contact is of the crimp type. Be careful of the applicable wire. 
2. The crimping contact crimps the covering in addition to the wire strand. Follow the dimensions listed above. 
An insulation of a smaller diameter may be able to be connected by a wire or tool, however. For details, contact 
Tyco Electronics Japan GK. 
3. To satisfy the TUV-approved and waterproof performance, a cable of an outer diameter within the applicable cable 
clamp range must be used. The connector kit includes rubber bushings (cable clamps). 
4. Dedicated tools are required for crimping and extracting the contact. Keep them on hand when required.
```

---

## 第 195 頁
**本頁字數:** 1059 字

### 內容摘要:
```text
able clamps). 
4. Dedicated tools are required for crimping and extracting the contact. Keep them on hand when required. 
(4) Connectors for power (Groups D to G) 
The power connectors alone in Groups D to G are TUV-approved and are waterproof in themselves (unengaged). 
Bayonet type and screw type are available. 
The specifications of each connector are explained based on the examples shown below. 
Besides, to meet the IEC60034 standard, TUV-approved plug connectors and cable clamps should be used in 
connecting the power line. To meet the IEC60034 standard by using a cable or conduit hose seal adapter, contact the 
manufacturer for details.

Ordering specification number of the power connector kit 
The specification numbers used for ordering a power connector kit from FANUC are listed below.

the power connector kit 
The specification numbers used for ordering a power connector kit from FANUC are listed below. The power 
connector kit contains a plug connector on the cable side (conforming to IP67, TUV-approved type) described 
subsequently.
```

---

## 第 196 頁
**本頁字數:** 799 字

### 內容摘要:
```text
182 
Bayonet type 
Group 
Power connector kit 
specifications 
Content 
D

A06B-6200-K810 
Single block type connector [D] 
Cable outer 
diameter 
φ11 to φ14.1 
A06B-6200-K811 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6200-K812 
Right angle type connector [B] 
+ cable clamp [C] 
F

A06B-6200-K813 
Single block type connector [D] 
Cable outer 
diameter 
For φ12.9 to 16 
A06B-6200-K814 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6200-K815 
Right angle type connector [B] 
+ cable clamp [C] 
Cable outer 
diameter 
For φ18 to 20 
A06B-6200-K822 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6200-K823 
Right angle type connector [B] 
+ cable clamp [C] 
Screw type 
Group 
Power connector kit 
specifications 
Content 
D

A06B-6079-K810 
Single block type connector [D]
```

---

## 第 196 頁
**本頁字數:** 1026 字

### 內容摘要:
```text
C] 
Screw type 
Group 
Power connector kit 
specifications 
Content 
D

A06B-6079-K810 
Single block type connector [D] 
Cable outer 
diameter 
For φ10.3 to 14.3 
A06B-6079-K811 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6079-K812 
Right angle type connector [B] 
+ cable clamp [C] 
F

A06B-6079-K813 
Single block type connector [D] 
Cable outer 
diameter 
For φ12.9 to 16 
A06B-6079-K814 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6079-K815 
Right angle type connector [B] 
+ cable clamp [C] 
Cable outer 
diameter 
For φ18 to 20 
A06B-6079-K822 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6079-K823 
Right angle type connector [B] 
+ cable clamp [C] 
G

A06B-6079-K816 
Single block type connector [D] 
Cable outer 
diameter 
For φ15 to 18 
A06B-6079-K817 
Straight

[C] 
G

A06B-6079-K816 
Single block type connector [D] 
Cable outer 
diameter 
For φ15 to 18 
A06B-6079-K817 
Straight type connector [A] 
+ cable clamp [C] 
A06B-6079-K818 
Right angle type connector [B] 
+ cable clamp [C]
```

---

## 第 198 頁
**本頁字數:** 561 字

### 內容摘要:
```text
184 
Power connector specifications (bayonet type) 
The specifications of manufacturers are shown below. For details of the connectors, contact each manufacturer.

Group 
[D] Single block type 
plug connector 
[A] Straight type 
plug connector 
[B] Right angle type 
plug connector 
[C] Cable clamp 
D 
(Japan Aviation Electronics Industry) 
JL10-6A18-10SE 
JL10-6A18-10SE-EB 
JL10-8A18-10SE-EB 
(a) JL04-18CK(07)-RK 
(b) JL04-18CK(10)-R 
(c) JL04-18CK(13)-R 
(d) JL04-18CK(15)-R 
Solder pot diameter φ2.8 
Applicable wire 3.5 mm2 or less 
Compatible cable O.D.
```

---

## 第 198 頁
**本頁字數:** 895 字

### 內容摘要:
```text
) JL04-18CK(13)-R 
(d) JL04-18CK(15)-R 
Solder pot diameter φ2.8 
Applicable wire 3.5 mm2 or less 
Compatible cable O.D. 
(a) φ5 to φ8 
(b) φ8 to φ11 
(c) φ11 to φ14.1 
(d) φ14.1 to φ15 
E 
(Japan Aviation Electronics Industry)

JL10-6A20-15SE(G)-
EB 
JL10-8A20-15SE(G)-
EB 
(a) JL04-2022CK(09)-R 
(b) JL04-2022CK(12)-R 
(c) JL04-2022CK(14)-R

Solder pot diameter φ2.8 (G terminal: φ5.3) 
Applicable wire 3.5 mm2 or less (G terminal: 8.0 mm2 or less) 
Compatible cable O.D. 
(a) φ6.5 to φ9.5 
(b) φ9.5 to φ13 
(c) φ12.9 to φ16 
F 
(Japan Aviation Electronics Industry) 
JL10-6A22-22SE 
JL10-6A22-22SE-EB 
(For (a) to (c)) 
JL10-6A22-22SE-EB1 
(For (d)) 
JL10-8A22-22SE-EB1 
(For (a) to (c)) 
JL10-8A22-22SE-EB1 
(For (d)) 
(a) JL04-2022CK(09)-R 
(b) JL04-2022CK(12)-R 
(c) JL04-2022CK(14)-R 
(d) JL04-2428CK(20)-RK 
Solder pot diameter φ5.3 
Applicable wire 10 mm2 or less 
Compatible cable O.D.
```

---

## 第 198 頁
**本頁字數:** 1161 字

### 內容摘要:
```text
04-2022CK(14)-R 
(d) JL04-2428CK(20)-RK 
Solder pot diameter φ5.3 
Applicable wire 10 mm2 or less 
Compatible cable O.D. 
(a) φ6.5 to φ9.5 
(b) φ9.5 to φ13 
(c) φ12.9 to φ16 
(d) φ18 to φ20 
* 
For the connectors of size 22-22, the parts model number of the plug connector differs depending on the type of 
cable clamp. 
* 
The items preceded by the same alphabet (a to d) in ( ) correspond to each other. 
Group 
[J] Low-profile angle type 
plug connector 
[K] Crimp 
socket contact 
[L] Solder 
socket contact 
[M] Bushing 
[N] O-ring 
D 
(Japan Aviation Electronics Industry) 
JL10-8A18-10SE-
LEB(☐☐)-A 
* 
☐☐ = S, SE, 
SW 
JL10S25 
HGH2 
JL10F01 
HGH1 
(a) JL10-18 
LEB-BSHG(09)-1 
(b) JL10-18 
LEB-BSHG(11)-1 
JL10-18 
LEB-ORING-1

Applicable wire 
1.25 to 2mm2 
Solder pot 
diameter 
φ2.6 
Applicable wire 
3.5 mm2 or less 
Compatible cable 
O.D.

G-1

Applicable wire 
1.25 to 2mm2 
Solder pot 
diameter 
φ2.6 
Applicable wire 
3.5 mm2 or less 
Compatible cable 
O.D. 
(a) φ8 to φ9.5 
(b) φ9.5 to φ11

The plug connectors and cable clamps listed above, when combined with the FANUC SERVO MOTOR αi-D series, 
satisfy the VDE0627 (EN61984) safety standard.
```

---

## 第 199 頁
**本頁字數:** 872 字

### 內容摘要:
```text
System configuration 
185 
Power connector specifications (screw type) 
The specifications of manufacturers are shown below. For details of the connectors, contact each manufacturer.

Group 
[D] Single block type 
plug connector 
[A] Straight type 
plug connector 
[B] Right angle type 
plug connector 
[B'] Low-profile 
 angle type 
plug connector 
(with clamp) 
[B''] Low-profile 
housing 
[C] Cable 
 clamp 
F 
(Japan Aviation Electronics Industry) 
JL04V-6A22- 
22SE-R 
(both (a) and 
(b)) 
(a) JL04V-
6A22- 
22SE-EB-R 
(b) JL04V-
6A22- 
22SE-EB1-R 
(a) JL04V-8A22- 
22SE-EBH-R 
(b) JL04V-8A22- 
22SE-EB1H-R

(a) JL04-22 
EBA-RK 
(b) Not 
supported

(a) JL04-
2022CK 
(14)-R 
(b) JL04-
2428CK 
(20)-RK 
Solder pot diameter φ5.3 
Applicable wire 10 mm2 or less 
(Applicable wire 5.5 mm2 or less In the case of single 
block + low-profile housing)

Compatible cable O.D.
```

---

## 第 199 頁
**本頁字數:** 867 字

### 內容摘要:
```text
mm2 or less 
(Applicable wire 5.5 mm2 or less In the case of single 
block + low-profile housing)

Compatible cable O.D. 
(a) φ12.9 to φ16 
(b) φ18 to φ20 
G 
(Japan Aviation Electronics Industry) 
JL04V-6A24- 
10SE(G)-R 
JL04V-6A24- 
10SE(G)-EB-R 
JL04V-8A24- 
10SE(G)-EBH-RK

JL04-24 
EBA-RK 
(c) JL04-
2428CK 
(17)-R 
(d) JL04-
2428CK 
(20)-R 
Solder pot diameter φ3.5 (G terminal: φ5.3) 
Applicable wire 5.5 mm2 or less (G terminal: 8.0 mm2 or 
less)

Compatible cable O.D. 
(c) φ15 to φ18 
(d) φ18 to φ20 
* 
For the connectors of size 22-22, the parts model number of the plug connector differs depending on the type of 
cable clamp. 
* 
For the connectors of size 24-10, the parts model number of the plug connector does not differ depending on the 
type of cable clamp. 
* 
The items preceded by the same alphabet (a to d) in ( ) correspond to each other. 
1.
```

---

## 第 199 頁
**本頁字數:** 489 字

### 內容摘要:
```text
g on the 
type of cable clamp. 
* 
The items preceded by the same alphabet (a to d) in ( ) correspond to each other. 
1. The plug connectors and cable clamps listed above, when combined with the FANUC SERVO MOTOR αi-D 
series, satisfy the VDE0627 (EN61984) safety standard. 
Plug connectors other than above are also available. For information about whether the plug connectors satisfy 
the safety standard when combined with the FANUC αi/βi series, contact the corresponding manufacturer.
```

---

## 第 200 頁
**本頁字數:** 858 字

### 內容摘要:
```text
186 
1.3.3. 
Connectors for the brake 
(1) Connectors for the brake (Group A) 
The motors in Group A use a TUV-approved dedicated connector to connect the integrated brake cable. 
The following subsection describes the specifications as a connector kit. These connectors are waterproof when 
engaged. 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp. Also note that there are restrictions.

Specifications of connectors for brake

For brake 
connector kit specifications 
A06B-6114-K272#E (FANUC specification) 
Contact specifications 
KN5FT02SJ1 (Japan Aviation Electronics Industry specification) 
Contact specifications 
C170-14-TMH5B (Japan Aviation Electronics Industry 
specification) 
Applicable wire size 
0.3 to 0.5mm2 (AWG#22 to 20) 
Insulation external diameter 
φ1.3 to φ1.4 
Compatible cable O.D.
```

---

## 第 200 頁
**本頁字數:** 1189 字

### 內容摘要:
```text
) 
Applicable wire size 
0.3 to 0.5mm2 (AWG#22 to 20) 
Insulation external diameter 
φ1.3 to φ1.4 
Compatible cable O.D. 
φ3.6 to φ4.8 
Tool for crimping terminal 
CT170-14-TMH5B (Japan Aviation Electronics Industry 
specification) 
A06B-6114-K273(FANUC specification)

1. No straight-type brake connectors are available. 
2. The contacts are of the type which crimps the covering in addition to the wire. Follow the dimension of the 
insulation part listed above. However, insulation of a diameter outside the above range may be connected 
depending on the wire or tool. For details, contact the connector manufacturer. 
3. No tool for pulling terminal out is used. 
(2) Connectors for the brake (Group B) 
The motors in Group B use a TUV-approved dedicated connector to connect the integrated brake cable. 
The following subsection describes the specifications as a connector kit.

nector to connect the integrated brake cable. 
The following subsection describes the specifications as a connector kit. These connectors are waterproof when 
engaged. 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp. Also note that there are restrictions.
```

---

## 第 201 頁
**本頁字數:** 897 字

### 內容摘要:
```text
System configuration 
187 
Specifications of connectors for brake

For brake 
connector kit specifications 
(Including the contact) 
Straight type 
2320298-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K262#S (FANUC specification) 
Right angle type 
2326774-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K262#E2 (FANUC specification) 
2379702-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K262#ED (FANUC specification) 
Applicable wire size 
0.13 to 0.33mm2 (AWG#26 to 22) 
Insulation external diameter 
φ1.0 to φ1.2 
Compatible cable O.D. 
φ4.5 to φ5.1 
Tool for crimping terminal 
1596847-1 (Tyco Electronics Japan GK specification) 
A06B-6114-K265#C (FANUC specification)

1. No straight-type brake connectors are available. 
2. The contacts are of the type which crimps the covering in addition to the wire. Follow the dimension of the 
insulation part listed above.
```

---

## 第 201 頁
**本頁字數:** 684 字

### 內容摘要:
```text
f the type which crimps the covering in addition to the wire. Follow the dimension of the 
insulation part listed above. However, insulation of a diameter outside the above range may be connected 
depending on the wire or tool. For details, contact the connector manufacturer. 
3. No tool for pulling terminal out is used. 
(3) Connectors for the brake (Group C) 
The motors in Group C use a TUV-approved dedicated connector to connect the integrated brake cable. 
The following subsection describes the specifications as a connector kit. These connectors are waterproof when 
engaged. 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp.
```

---

## 第 201 頁
**本頁字數:** 1261 字

### 內容摘要:
```text
rproof when 
engaged. 
To connect the cable, a dedicated crimping tool must be used. 
Consider crimping and cable clamp. Also note that there are restrictions.

Specifications of connectors for brake

For brake 
connector kit specifications 
(Including the contact) 
Straight type 
2320298-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K262#S (FANUC specification) 
Right angle type 
2379702-2 (Tyco Electronics Japan GK specification) 
A06B-6114-K262#ED (FANUC specification) 
Applicable wire size 
0.13 to 0.33mm2 (AWG#26 to 22) 
Insulation external diameter 
φ1.0 to φ1.2 
Compatible cable O.D. 
φ4.5 to φ5.1 
Tool for crimping terminal 
1596847-1 (Tyco Electronics Japan GK specification) 
A06B-6114-K265#C (FANUC specification)

1. No straight-type brake connectors are available. 
2. The contacts are of the type which crimps the covering in addition to the wire.

type brake connectors are available. 
2. The contacts are of the type which crimps the covering in addition to the wire. Follow the dimension of the 
insulation part listed above. However, insulation of a diameter outside the above range may be connected 
depending on the wire or tool. For details, contact the connector manufacturer. 
3. No tool for pulling terminal out is used.
```

---

## 第 202 頁
**本頁字數:** 800 字

### 內容摘要:
```text
188 
(4) Connectors for the brake (Groups D to G) 
The motors in Groups D to G use a TUV-approved dedicated connector to connect the integrated brake cable. 
This connector is waterproof. It is connected by soldering, so no special tool is required. 
Consider soldering, cable clamp, and voltage drop. Also note that there are restrictions.

Specifications of connectors for brake

Japan Aviation Electronics Industry 
Hirose Electric 
Contact 
specificat
ions 
Straight 
type 
JN2DS04FKK-R (Japan Aviation 
Electronics Industry specification) 
A06B-6114-K213#S (FANUC 
specification) 
HR34B-12WPD-4S (Hirose Electric 
specification) 
HR34B-12WPE-4S (Hirose Electric 
specification) 
Right angle 
type 
JN2FS04FKK-R (Japan Aviation 
Electronics Industry specification) 
A06B-6114-K213#E (FANUC 
speci
```

---

## 第 202 頁
**本頁字數:** 774 字

### 內容摘要:
```text
n) 
Right angle 
type 
JN2FS04FKK-R (Japan Aviation 
Electronics Industry specification) 
A06B-6114-K213#E (FANUC 
specification) 
HR34B-12WLPD-4S (Hirose Electric 
specification) 
HR34B-12WLPE-4S (Hirose Electric 
specification) 
Compatible cable 
AWG#16 or less (1.25 mm2 or less) 
(Solder pot diameter: φ1.9) 
Insulation external 
diameter 
φ2.7 or less 
Compatible cable O.D. 
φ6.5 to φ8.0 
φ5.7 to φ7.3 
(For HR34B-12WPD-4S, HR34B-12WLPD-4S) 
φ6.5 to φ8.0 
(For HR34B-12WPE-4S, HR34B-12WLPE-4S) 
Example of applicable 
wire 
300-V sheathed cable 
VCTF 2-core (JIS C 3306) or equivalent 
Compatible cable 
and cable length 
Cable length of 30 m or less : 0.75 mm2 (AWG#18) 
Cable length of 50 m or less : 1.25 mm2 (AWG#16)

ble length of 50 m or less : 1.25 mm2 (AWG#16)
```

---

## 第 203 頁
**本頁字數:** 558 字

### 內容摘要:
```text
System configuration 
189 
Japan Aviation Electronics Industry

1. The same housing is used for the connector for brakes and cooling fans and that of signals. They differ in the 
number of cores and key position. For connector engagement, see "II.1.3.1. Connectors for signals (for all αi-D series 
models).(P.176)" 
2. If the cable length is longer than or equal to 50 m, take measures such as installation of repeaters so that the sum 
of wire resistance (for both ways) becomes 1.5 Ω or less. 
3. For details of brakes, see "I.3.3. Built-in brake(P.149)."
```

---

## 第 204 頁
**本頁字數:** 800 字

### 內容摘要:
```text
190 
1.3.4. 
Cooling fan connector 
αiS50 FAN-D, αiS60 FAN-D, and αiF40 FAN-D (including HV) use dedicated connectors which are TUV approved for 
the connection between a cooling fan and the power supply for the cooling fan. 
This connector is waterproof. It is connected by soldering, so no special tool is required. 
Consider soldering, cable clamp, and voltage drop. Also note that there are restrictions.

Specifications of cooling fan connectors

Japan Aviation Electronics Industry 
Hirose Electric 
Contact 
specificat
ions 
Straight 
type 
JN2DS04FKKX-R (Japan Aviation 
Electronics Industry specification) 
A06B-6114-K214#S (FANUC specification) 
HR34B-12WPD-4S-X (Hirose Electric) 
HR34B-12WPE-4S-X (Hirose Electric) 
Right angle 
type 
JN2FS04FKKX-R (Japan Aviation 
Electronics Industry s
```

---

## 第 204 頁
**本頁字數:** 689 字

### 內容摘要:
```text
Electric) 
HR34B-12WPE-4S-X (Hirose Electric) 
Right angle 
type 
JN2FS04FKKX-R (Japan Aviation 
Electronics Industry specification) 
A06B-6114-K214#E (FANUC specification) 
HR34B-12WLPD-4S-X (Hirose Electric) 
HR34B-12WLPE-4S-X (Hirose Electric) 
Compatible cable 
AWG#16 or less (1.25 mm2or less) 
(Solder pot diameter: φ1.9) 
Insulation external 
diameter 
φ2.7 or less 
Compatible cable O.D. 
φ6.5 to φ8.0 
φ5.7 to φ7.3 
(For HR34B-12WPD-4S-X, 
HR34B-12WLPD-4S-X) 
φ6.5 to φ8.0 
(For HR34B-12WPE-4S-X, 
HR34B-12WLPE-4S-X) 
Example of applicable 
wire 
300-V sheathed cable 
VCTF 3-core (JIS C 3306) or equivalent 
Recommended wire 
size and cable length 
0.5 mm2 or more (AWG#20)

#20)
```

---

## 第 205 頁
**本頁字數:** 561 字

### 內容摘要:
```text
System configuration 
191 
Japan Aviation Electronics Industry

1. The same housing is used for the connector for brakes and cooling fans and that of signals. They differ in the 
number of cores and key position. For connector engagement, see "II.1.3.1. Connectors for signals (for all αi-D series 
models).(P.176)" 
2. If the cable length is longer than or equal to 50 m, take measures such as installation of repeaters so that the sum 
of wire resistance (for both ways) becomes 1.5 Ω or less. 
3. For details of cooling fans, see "I.3.4. Cooling fan(P.156)."
```

---

## 第 206 頁
**本頁字數:** 521 字

### 內容摘要:
```text
192 
1.3.5. 
Caution 
Direction of pulling out cable 
The directions of pulling out cable for Groups A to C are shown below.

Direction of pulling out cable (Group A) 
The directions of pulling out cable for Group A are shown below.  
Recommended direction of pulling out cable

Unusable direction of pulling-
out 
Pulsecoder cable

Direction of pulling out cable (Group B) 
The directions of pulling out cable for Group B  
Recommended direction of pulling out cable

Unusable direction of pulling-
out 
Pulsecoder cable
```

---

## 第 207 頁
**本頁字數:** 603 字

### 內容摘要:
```text
System configuration 
193 
Direction of pulling out cable (Group C) 
The directions of pulling out cable for Group C are shown below.  
Recommended direction of pulling out cable

Unusable direction of pulling-
out 
Pulsecoder cable

For convenience, the figures show connectors directed horizontally. 
If a connector is used facing upward, the cutting fluid moves along the cable and collects into the connector, so face it 
horizontally or downward as much as possible. 
If it is faced horizontally, this can be prevented by taking further measures such as forming a slack in some parts of the 
cable.
```

---

## 第 208 頁
**本頁字數:** 407 字

### 內容摘要:
```text
194 
How to handle cables 
Due to flapping of the cable, load is applied to the connector, and when the mating part is shaken repeatedly, it may 
lead to connection failure or degradation of waterproof performance. 
Take appropriate measures such as fixing the cable to the machine so as not to apply load to the connector. 
As a guide, fix the cable at the position approximately 100 mm from the connector.
```

---

## 第 209 頁
**本頁字數:** 1120 字

### 內容摘要:
```text
System configuration 
195 
Differences from previous models

αiS 0.5-D and αiS 1-D 
The power connectors and brake connectors of αiS 0.5-D and αiS 1-D are not compatible with βiS 0.5/6000-B (A06B-
2115-Bxxx) or βiS 1/6000-B (A06B-2116-Bxxx). 
Model 
(Specification number) 
αiS 0.5/8000-D (A06B-3015-Bxxx) 
αiS 1/8000-D (A06B-3017-Bxxx) 
βiS 0.5/6000-B (A06B-2115-Bxxx) 
βiS 1/6000-B (A06B-2116-Bxxx) 
Manufacturer 
MOLEX JAPAN Co., Ltd. 
(one-touch type) 
Manufacturer: MOLEX JAPAN Co., Ltd. 
(screw fix type) 
Manufacturer specification 
Power: 2822926-1 
Brake: 2304867-1 
Power: 55618-0403 
Brake: 55619-0401 
Appearance

αiS 2-D, αiS 4-D, αiS 2HV-D, αiS 4HV-D, αiF 1-D, and αiF 2-D 
The power connectors and brake connectors of αiS 2-D, αiS 4-D, αiS 2HV-D, αiS 4HV-D, αiF 1-D and αiF 2-D are 
different from the αi-B/βi-B series (screw fix type) in connection/disconnection method.

4HV-D, αiF 1-D and αiF 2-D are 
different from the αi-B/βi-B series (screw fix type) in connection/disconnection method.  
Model 
αi-D series 
(one-touch type) 
αi-B/βi-B series 
(screw fix type) 
Connection/disconnection 
direction
```

---

## 第 210 頁
**本頁字數:** 768 字

### 內容摘要:
```text
196 
1.4. 
Compliance with safety standards 
The FANUC SERVO MOTOR αi-D series are designed to comply with safety standard EN60034-1. 
To prove this compliance, they are approved by TÜV Rheinland, a third-party certification body. 
1.4.1. 
Specifications of EN60034-1-compliant motors 
The following motor specifications are approved for the EN60034-1 standard.

(1) Rotation speed (EN60034-1) 
The "rated rotation speed" and "allowable maximum rotation speed" are given on the data sheet in "I. 
specifications(P.1)." 
"Rated rotation speed" is the maximum rotation speed in continuous characteristics. 
The maximum rotation speeds are specified in such a way that the approval conditions of the EN60034-1 standard, 
as they relate to rotational speed, are satisfied.
```

---

## 第 210 頁
**本頁字數:** 696 字

### 內容摘要:
```text
n such a way that the approval conditions of the EN60034-1 standard, 
as they relate to rotational speed, are satisfied. When the allowable maximum speeds are used, the characteristics 
are not guaranteed.

(2) Output (EN60034-1) 
The "rated output" available with a motor is given on the data sheet in "I. specifications(P.1)." The rated output is 
guaranteed as continuous maximum output under Insulation Class F. 
The output in an intermittent operation range is not specified.

(3) Protection class (EN60034-5) 
Motor protection conforms to IP67. (except the models with a cooling fan) 
Motor protection of models with cooling fan conforms to IP67 except the fan motor and the fan connectors.
```

---

## 第 210 頁
**本頁字數:** 872 字

### 內容摘要:
```text
cooling fan) 
Motor protection of models with cooling fan conforms to IP67 except the fan motor and the fan connectors. 
The protection types mentioned above do not apply to the part that the motor axis penetrates.

IP6○   :  Fully dust-proof machine 
Structure completely free from the entry of dust.

IP○7   :  Machine protected from the effect of seeping water 
If the machine is submerged in water at a prescribed pressure for a prescribed duration, an amount of water that has 
a harmful impact on the machine does not enter the machine.

Requirements for IP○7 certification test 
The motor must be completely submerged in water so that the following conditions are satisfied. 
- The water surface is at least 150 mm above the top of the motor. 
- The bottom end of the motor is at least 1 m below the water surface. 
- The motor is submerged for at least 30 minutes.
```

---

## 第 210 頁
**本頁字數:** 506 字

### 內容摘要:
```text
The bottom end of the motor is at least 1 m below the water surface. 
- The motor is submerged for at least 30 minutes. 
- The difference between the water temperature and the motor temperature does not exceed 5°C. 
IP○7 evaluates machines for waterproofness in a short-term test as described above. 
If a machine is exposed to or submerged in liquids other than water for a long period of time, it may suffer harmful 
effect. 
(4) Cooling method (EN60034-6) 
The motor cooling methods are as listed below.
```

---

## 第 211 頁
**本頁字數:** 451 字

### 內容摘要:
```text
System configuration 
197 
Model 
IC code 
Method 
αiS 50/3000 FAN-D 
αiS 60/3000 FAN-D 
αiF 40/3000 FAN-D 
(including HV) 
IC416 
Fully closed; Air-cooled by an external independence 
fan 
Models except for the above 
IC410 
Fully closed; cooled by a natural air flow

(5) Mounting method (EN60034-7) 
For αiS 2-D to αiS 60-D, αiS 2HV-D to αiS 60HV-D, αiF 1-D to αiF 40-D, and αiF 4HV-D to αiF 40HV-D, motors can 
be mounted in the following methods.
```

---

## 第 211 頁
**本頁字數:** 1081 字

### 內容摘要:
```text
2HV-D to αiS 60HV-D, αiF 1-D to αiF 40-D, and αiF 4HV-D to αiF 40HV-D, motors can 
be mounted in the following methods. 
IMB5: Flange mounting with the shaft facing sideways (from the rear) 
IMV1: Flange mounting with the shaft facing downward (from the rear) 
IMV3: Flange mounting with the shaft facing upward (from the rear)

(6) Heat protection (EN60034-11) 
The FANUC servo motors conforms to the heat protection standard (EN60034-11) by using a protection circuit from 
over heat with temperature detection (overheat alarm) or a protection circuit from over heat with current detection 
(OVC alarm).

(7) Grounding (EN60204-1) 
For FANUC servo motors, continuity between the earth terminal and housing of the power connector has been 
checked based on the EN60204-1 safety standard and it has been ensured that it satisfies the standard.

nnector has been 
checked based on the EN60204-1 safety standard and it has been ensured that it satisfies the standard. 
The earth line to be connected to the motor must have a diameter not smaller than the diameter of each phase wire.
```

---

## 第 212 頁
**本頁字數:** 694 字

### 內容摘要:
```text
198 
1.4.2. 
For compliance with CE marking of machines and devices 
(1) For compliance with EMC Directives 
For details on EMC compliance authorization, refer to the separate manual "Compliance with EMC Directives (A-
72973JA)." 
Mechanical and electrical safety of each motor should be evaluated after the motor is mounted on the machine.

(2) For the protection of motors from overvoltage 
If the power supply input unit of the machine does not have an isolation transformer, it is necessary to use an 
EN61643-11-compliant lightning surge protector with a voltage protection level of 1.5 kV or less for 200-V systems 
and 2.5 kV or less for 400-V systems to protect motors from overvoltage.
```

---

## 第 212 頁
**本頁字數:** 1234 字

### 內容摘要:
```text
tion level of 1.5 kV or less for 200-V systems 
and 2.5 kV or less for 400-V systems to protect motors from overvoltage. 
See "SERVO AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN) for details about installing lightning surge 
protectors.

(3) Connectors 
The power and cooling fans for a motor need to be connected with connectors and cable clamps certified to 
European standards by a third-party certification body. 
Refer to "II.1.1. Connecting a servo motor(P.169)" for details. 
 
TUV have certified that the TUV-approved plug connectors and cable clamps of "II.1.3. Connectors on the cable 
side(P.175)", when combined with the FANUC SERVO MOTOR αi-D series, satisfy the VDE0627 (EN61984) 
safety standard. 
Several manufacturers offer plug connectors other than above.

D series, satisfy the VDE0627 (EN61984) 
safety standard. 
Several manufacturers offer plug connectors other than above. For information about whether the plug connectors 
satisfy the safety standard when combined with the FANUC SERVO MOTOR αi-D series, contact the corresponding 
manufacturer. Contact the manufacturers if you require details of their products.

 
If a cable or conduit hose seal adapter is used, consult an appropriate connector maker.
```

---

## 第 213 頁
**本頁字數:** 749 字

### 內容摘要:
```text
Motor selection 
199 
2. 
Motor selection 
Use the servo selection tool Servo Sizer by FANUC to select a servo motor. Servo Sizer allows you to easily select 
the best-suited servo motor by following the procedure displayed on the screen and entering values. 
Besides, you can select various motors, such as the best-suited drive amplifier, Power Supply, and spindle motor. 
Servo Sizer can be downloaded for free from the FANUC member's website: https://store.member.fanuc.co.jp/fanuc/store. 
If you want to select a servo motor by manual calculation without using Servo Sizer, refer to the following procedure 
in the selection examples. 
The selection of the servo motor is based on theoretical calculation: it does not guarantee operation. 
2.1.
```

---

## 第 213 頁
**本頁字數:** 849 字

### 內容摘要:
```text
examples. 
The selection of the servo motor is based on theoretical calculation: it does not guarantee operation. 
2.1. 
Conditions for selecting a servo motor 
[Selection condition 1] Steady-state load torque 
 
The steady-state load torque including mechanical friction and gravity must fall within approximately 70% of the 
continuous torque (at low speed) of a motor. 
If the steady-state load torque is close to the continuous torque (at low speed), the root-mean-square value of the 
total torque including the acceleration torque is more likely to exceed the continuous torque (at low speed). 
Along the vertical axis, the load may be increased during lifting and at stop due to a mechanical factor. In this case, 
the theoretically calculated gravity retaining torque must be 60% or less of the continuous torque (at low speed) of a 
motor.
```

---

## 第 213 頁
**本頁字數:** 743 字

### 內容摘要:
```text
eoretically calculated gravity retaining torque must be 60% or less of the continuous torque (at low speed) of a 
motor. 
The figure of "within approximately 70% of the continuous torque (at low speed)" is for reference only. Determine the 
appropriate torque based upon actual machine tool conditions.

[Selection condition 2] Rotation speed 
 
The rotation speed must not exceed the maximum rotation speed (rated speed during continuous operation). 
Calculate the rotation speed and check that the speed does not exceed the maximum rotation speed. For continuous 
operation, check that the speed does not exceed the rated speed.

[Selection condition 3] Load moment of inertia ratio 
 
The load moment of inertia ratio must be appropriate.
```

---

## 第 213 頁
**本頁字數:** 703 字

### 內容摘要:
```text
d speed.

[Selection condition 3] Load moment of inertia ratio 
 
The load moment of inertia ratio must be appropriate. (recommended ratio is three times or less) 
The ratio of moment of inertia of rotor and load moment of inertia (load moment of inertia ratio) greatly affects the 
controllability of the motor as well as the acceleration/deceleration time. 
As long as the load moment of inertia does not exceed three times the moment of inertia of rotor, the motor can be 
used without problems, while the controllability may have to be lowered a little due to the rigidity of the machine shaft.

[Selection condition 4] Acceleration torque 
 
Acceleration can be made with a desired time constant.
```

---

## 第 213 頁
**本頁字數:** 817 字

### 內容摘要:
```text
e machine shaft.

[Selection condition 4] Acceleration torque 
 
Acceleration can be made with a desired time constant. 
Since the load torque generally helps deceleration, if acceleration can be executed with a desired time constant, 
deceleration can be made with the same time constant, through both acceleration and deceleration should be 
considered in principle. Calculate the acceleration torque and check that the torque required for acceleration is within 
the intermittent operating zone of the motor. 
Allowing a margin of about 10% is recommended during check.

[Selection condition 5] Root-mean-square value of torque 
 
The root-mean-square value of torque in a cycle must be sufficiently greater than the continuous torque (at low 
speed). 
A motor gets hot in proportion to the square of the torque.
```

---

## 第 213 頁
**本頁字數:** 463 字

### 內容摘要:
```text
ciently greater than the continuous torque (at low 
speed). 
A motor gets hot in proportion to the square of the torque. For a servo motor for which the load condition always 
changes, the calculated root-mean-square value of torque in a cycle must be sufficiently greater than the continuous 
torque (at low speed). 
Pay attention, in particular, when the cutting load, acceleration/deceleration condition, and other load conditions 
variously change in a cycle.
```

---

## 第 214 頁
**本頁字數:** 731 字

### 內容摘要:
```text
200 
When the desired frequency of positioning in rapid traverse becomes greater, the ratio of the time during which the 
acceleration/deceleration torque is being applied to the entire operation time increases and the root-mean-square 
value of torque increases. In this case, increasing the acceleration/deceleration time constant is effective to decrease 
the root-mean-square value of torque.

[Selection condition 6] Percentage duty cycle and ON time with the maximum cutting torque 
 
The time during which the maximum cutting torque can be applied (percentage duty cycle and ON time) must be 
within a desired range. 
The continuously applied torque such as the cutting load may exceed the continuous torque (at low speed).
```

---

## 第 214 頁
**本頁字數:** 844 字

### 內容摘要:
```text
esired range. 
The continuously applied torque such as the cutting load may exceed the continuous torque (at low speed). In this 
case, use overload duty curves to check how the ratio (percentage duty cycle) of the load applying time to the no-load 
applying time and the time during which the load is being applied (ON time) change.

[Selection condition 7] Dynamic brake stop distance 
 
The stop distance when the dynamic brake is applied at emergency stop condition must be within a desired 
range. 
If the stop distance is not within the desired range, the machine may cause a collision at emergency stop condition.

Along the vertical axis (for motors with a brake)

[Selection condition 8] Brake retaining torque 
 
The load torque should be within the brake retaining torque. 
If this cannot be satisfied, set the counter balance etc.
```

---

## 第 214 頁
**本頁字數:** 989 字

### 內容摘要:
```text
The load torque should be within the brake retaining torque. 
If this cannot be satisfied, set the counter balance etc. 
It is recommended to use the motor with not more than 70% of the brake holding torque.

The following chapters explain the procedure for selecting a motor sequentially for each selection condition. Check 
that the selection conditions 1 to 7 above are satisfied.

NOTE 
When handling units, be extremely careful not to use different systems of units. For example, the weight of an object 
should be expressed in [kg] in the SI unit because it is handled as "mass" or [kgf] in the gravitational system of units 
because it is handled as "force." Moment of inertia is expressed in [kg·m2] in the SI system of units or in [kgf·cm·s2] in 
the gravitational system of units.

nt of inertia is expressed in [kg·m2] in the SI system of units or in [kgf·cm·s2] in 
the gravitational system of units. 
In this manual, both systems of units are written together to support them.
```

---

## 第 215 頁
**本頁字數:** 800 字

### 內容摘要:
```text
Motor selection 
201 
2.2. 
Selecting a motor 
Sample model for calculations for selecting a servo motor

The following chapters explain how to calculate conditions for selecting a servo motor best suited for a table with a 
horizontal axis with the following specifications.

Sample mechanical specifications and calculated values of the table and workpiece 
W : Weight of movable parts (table and workpiece) = 11760 [N] = 1200 [kgf] 
w : Mass of movable parts (table and workpiece) = 1200 [kg] 
μ : Friction coefficient of the sliding surface = 0.05 
η : Efficiency of the driving system (including a ball screw) = 0.9 
Fg : Gib fastening force (kgf) = 490 [N] = 50 [kgf] 
Fc : Thrust counterforce caused by the cutting force (kgf) = 4900 [N] = 500 [kgf] 
Fcf: Force by which the table is pressed a
```

---

## 第 215 頁
**本頁字數:** 1071 字

### 內容摘要:
```text
Thrust counterforce caused by the cutting force (kgf) = 4900 [N] = 500 [kgf] 
Fcf: Force by which the table is pressed against the sliding surface, caused by the moment of cutting force = 294 [N] = 
30 [kgf] 
Z1/Z2 : Gear reduction ratio = 1/1 
Tbf : Friction torque applied to the motor shaft = 0.8 [N⋅m] = 8 [kgfcm]

Sample specifications and calculated values of the feed screw (ball screw) 
Db : Shaft diameter = 40 × 10-3 [m] = 40 [mm] 
Lb : Shaft overall length = 1 [m] = 1000 [mm] 
P : Pitch = 20 × 10-3 [m/rev] 
= 20 [mm/rev]

Sample specifications and calculated values of the operation of the motor shaft 
Ta : Acceleration torque [N⋅m][kgf⋅cm] 
V : Workpiece rapid traverse rate = 60 [m/min] 
Vm : Motor speed in rapid traverse [min-1] 
ta : Acceleration time = 0.07 [s] 
JM : Moment of in

erse rate = 60 [m/min] 
Vm : Motor speed in rapid traverse [min-1] 
ta : Acceleration time = 0.07 [s] 
JM : Moment of inertia of rotor (rotor inertia) [kg⋅m2] [kgf⋅cm⋅s2] 
JL : Load moment of inertia (load inertia) [kg⋅m2] [kgf⋅cm⋅s2] 
ks : Position loop gain =30 [s-1]
```

---

## 第 216 頁
**本頁字數:** 678 字

### 內容摘要:
```text
202 
2.2.1. 
Calculating the load torque 
When a part moves along an axis at a constant speed, the torque obtained by multiplying the weight of the workpiece 
driving section by the friction coefficient is always applied. On a vertical or slanted axis, the motor keeps producing 
torque because it works against gravity. In addition, the motor also produces torque when the machine on the 
horizontal axis stops in proportion to the load friction. This continuously applied load torque is the steady-state load 
torque. 
In cutting feed, the load torque is applied by cutting thrust. This is the cutting torque. 
The above types of torque are generically called the load torque.
```

---

## 第 216 頁
**本頁字數:** 800 字

### 內容摘要:
```text
pplied by cutting thrust. This is the cutting torque. 
The above types of torque are generically called the load torque. The load torque applied to the motor shaft is 
generally calculated by the following equation:

Tm : Load torque applied to the motor shaft [N⋅m] 
F: Force required to move a movable part (table or tool post) along the axis [N] 
l : Stroke of the machine tool per revolution of the motor = P × (Z1/Z2) [m/rev] 
η : Efficiency of the driving system (including a ball screw) 
Tf : Friction torque of the nut of the ball screw or bearing applied to the motor shaft (input if necessary) [N⋅m]

The force (F) is mainly calculated by the following equations: 
When cutting is not executed (vertical axis): 
F = (w − wc)g = W − Wc 
wc : Mass of the counterbalance [kg] 
Wc : Weight of t
```

---

## 第 216 頁
**本頁字數:** 885 字

### 內容摘要:
```text
cutting is not executed (vertical axis): 
F = (w − wc)g = W − Wc 
wc : Mass of the counterbalance [kg] 
Wc : Weight of the counterbalance [kgf] 
When cutting is not executed (horizontal axis): 
F = μ(W + Fg) 
When cutting is in progress (horizontal axis) (constant load + cutting thrust): 
F=Fc+μ(W+Fg+Fcf)

[Example of calculation for condition 1] Steady-state load torque 
For a table with a horizontal axis as given as a model, the steady-state load torque when cutting is not executed is 
calculated as follows:

Example: F = 0.05 × (11760 + 490) = 612.5 [N] = 62.5 [kgf] 
Tm = (612.5 × 20 × 10-3 × 1) ÷ (2 × π × 0.9) + 0.8 
=3.0 [Nm] = 30.6 [kgfcm]

Cautions in calculating the load torque 
 
Allow for the friction torque caused by the gib fastening force (Fg). 
The torque calculated only from the weight of a movable part and the friction coefficient is generally quite small.
```

---

## 第 216 頁
**本頁字數:** 894 字

### 內容摘要:
```text
g). 
The torque calculated only from the weight of a movable part and the friction coefficient is generally quite small. 
The gib fastening force and accuracy of the sliding surface may have a great effect on the torque. 
 
The pre-load of the bearing or nut of the ball screw, pre-tension of the screw, and other factors may make friction 
torque Tbf of the rolling contact considerable. In a small, lightweight machine tool, the friction torque will greatly 
affect the entire torque. 
 
Allow for an increase in friction on the sliding surface (Fcf) caused by the cutting resistance. 
The cutting resistance and the driving force generally do not act through a common point as illustrated below. 
When a large cutting resistance is applied, the moment increases the load on the sliding surface. When 
calculating the torque during cutting, allow for the friction torque caused by the load.
```

---

## 第 216 頁
**本頁字數:** 694 字

### 內容摘要:
```text
d on the sliding surface. When 
calculating the torque during cutting, allow for the friction torque caused by the load. 
 
The feedrate may cause the friction torque to vary greatly. Obtain an accurate value by closely examining 
variations in friction depending on variations in speed, the mechanism for supporting the table (sliding contact, 
rolling contact, static pressure, etc.), material of the sliding surface, lubricating system, and other factors. 
 
The friction torque of a single machine varies widely due to adjustment conditions, ambient temperature, and 
lubrication conditions. Collect a great amount of measurement data of identical models so as to apply as correct

orrect
```

---

## 第 217 頁
**本頁字數:** 872 字

### 內容摘要:
```text
Motor selection 
203 
values as possible when calculating load torque. When adjusting the gib fastening force and backlash, monitor the 
friction torque. Avoid generating an unnecessarily great torque. 
2.2.2. 
Calculating the rotation speed 
Calculate the rotation speed using the movable part rapid traverse rate and stroke per revolution of the motor and 
check that the calculated rotation speed does not exceed the maximum rotation speed of the motor (rated speed for 
continuous operation).

Vm : Motor speed in rapid traverse [min-1] 
V: Workpiece rapid traverse rate [m/min] 
l : Stroke per revolution of the motor [m/rev] = P
Z1/Z2

[Example of calculation for condition 2] Rotation speed 
Example: V=60[m/min], l=P Z1/Z2=0.020 1/1=0.020[m/rev] 
Vm is 60/0.020 = 3000 [min-1]. This value does not exceed the rated speed of the αiS22/4000-D provisionally selected.
```

---

## 第 217 頁
**本頁字數:** 856 字

### 內容摘要:
```text
] 
Vm is 60/0.020 = 3000 [min-1]. This value does not exceed the rated speed of the αiS22/4000-D provisionally selected. 
Then, select a motor whose load torque when cutting is not executed (continuous torque (at low speed)) is 3.0 [N⋅m] 
and whose maximum rotation speed is at least 3000 [min-1] from the data sheet. The αiS22/4000-D (with a continuous 
torque (at low speed) of 22 [N⋅m]) is provisionally selected in light of the acceleration/deceleration condition 
described in the following subsection. 
2.2.3. 
Calculating the load moment of inertia 
Unlike the load torque, an accurate load moment of inertia can be obtained just by calculation. The moment of inertia 
of any object moved by the revolution of a driving motor forms the load moment of inertia of the motor, regardless of 
whether the object is rotated or moved along a straight line.
```

---

## 第 217 頁
**本頁字數:** 914 字

### 內容摘要:
```text
ms the load moment of inertia of the motor, regardless of 
whether the object is rotated or moved along a straight line. The load moment of inertia can be obtained by 
calculating the moment of inertia of each driven object individually and adding all those moment values according to a 
set of rules. The moment of inertia of almost all objects, including the basic examples shown below, can be calculated 
in this way.

Moment of inertia of a cylindrical object (ball screw, gear, coupling, etc.)

The moment of inertia of a cylindrical object rotating about its central axis is calculated as follows: 
-SI unit--------------------------- 
  [kg⋅m2] 
Jb : Moment of inertia [kg⋅m2] 
γb : Mass of the object per unit volume [kg/m3] 
Db : Diameter of the object [m] 
Lb : Length of the object [m]

m2] 
γb : Mass of the object per unit volume [kg/m3] 
Db : Diameter of the object [m] 
Lb : Length of the object [m]
```

---

## 第 218 頁
**本頁字數:** 931 字

### 內容摘要:
```text
revolution of the motor [m]

-Gravitational system of units-------------------------- 
  [kgf⋅cm⋅s2] 
W : Weight of the object moving along a straight line [kgf] 
l : Traveling distance along a straight line per revolution of the motor [cm]

[Example of calculation for condition 3-2] Load moment of inertia 
Example: When w is 1200 [kg] and l is 20 [mm], the moment of inertia Jw of a table and workpiece is calculated as 
follows: 
Jw = 1200 × (0.020 ÷ 2 ÷ π)2 = 0.01216 [kg⋅m2] = 0.1241 [kgf⋅cm⋅s2]

Moment of inertia of an object whose speed is decelerated or accelerated with respect to the 
motor shaft

The moment of inertia applied to the motor shaft for J0 is calculated as follows:

J0 : Moment of inertia before deceleration 
Z1, Z2 : Number of teeth when the gear connection 
1/Z : Reduct

as follows:

J0 : Moment of inertia before deceleration 
Z1, Z2 : Number of teeth when the gear connection 
1/Z : Reduction ratio
```

---

## 第 219 頁
**本頁字數:** 890 字

### 內容摘要:
```text
Motor selection 
205 
Moment of inertia of a cylindrical object whose rotation center is displaced

J0 : Moment of inertia around the center of the cylindrical object 
M : Weight of the object 
R : Radius of rotation

The above equation is used for such purposes as to calculate the moment of inertia of a large gear which is hollowed 
out in order to reduce the moment of inertia and weight. 
The sum of the moment of inertia calculated above is the load moment of inertia J for accelerating the motor.

- Cautions regarding the limitations on the load moment of inertia 
For example, if the load moment of inertia becomes greater, a change in the specified speed causes the motor to 
take more time to reach the new specified speed. When a machine tool is moved along two axes at a high speed to 
cut a curve such as an arc, a larger error occurs than if the moment of inertia is smaller.
```

---

## 第 219 頁
**本頁字數:** 824 字

### 內容摘要:
```text
two axes at a high speed to 
cut a curve such as an arc, a larger error occurs than if the moment of inertia is smaller. 
There are limitations on the load moment of inertia ratio when the dynamic brake is used. For details about the 
limitations, see "II.2.2.7. Calculating the dynamic brake stop distance(P.213)."

[Example of calculation for condition 3-3] Load moment of inertia ratio 
Since the sum of Jb and Jw obtained in calculation examples 3-1 and 3-2 is the load moment of inertia JL, the load 
moment of inertia can be calculated as follows: 
JL = 0.00196 + 0.01216 = 0.01412 [kgm2] 
Since the moment of inertia of rotor of αiS22/4000-D is 0.0053 [kgm2], the load moment of inertia ratio is 2.7 times, 
which is within the allowable range.

nt of inertia ratio is 2.7 times, 
which is within the allowable range.
```

---

## 第 220 頁
**本頁字數:** 683 字

### 內容摘要:
```text
206 
2.2.4. 
Calculating the acceleration torque 
Calculate the acceleration torque required for the motor to accelerate and then obtain the torque required for 
acceleration by calculating the total torque including the steady-state load torque calculated before. Next, confirm the 
result is included in the intermittent operation area for the motor. 
(1) Calculating acceleration torque 
Calculate the angular acceleration, based on the assumption that the motor shaft operates ideally in the 
acceleration/deceleration type. Multiply the angular acceleration by the total moment of inertia (moment of inertia of 
rotor + load moment of inertia) to obtain the acceleration torque.
```

---

## 第 220 頁
**本頁字數:** 466 字

### 內容摘要:
```text
by the total moment of inertia (moment of inertia of 
rotor + load moment of inertia) to obtain the acceleration torque. 
For the acceleration/deceleration type at the time of rapid traverse, there are the linear type and the bell type, and the 
following shows the equations for acceleration torque used in each case.

Acceleration torque in linear acceleration/deceleration

When the torque is Ta and the speed is Vr in the above figure, torque is needed the most.
```

---

## 第 220 頁
**本頁字數:** 1214 字

### 內容摘要:
```text
ear acceleration/deceleration

When the torque is Ta and the speed is Vr in the above figure, torque is needed the most. The equations for 
calculating Ta and Vr are given below:

Ta : Acceleration torque [Nm] 
Vm : Motor speed in rapid traverse [min-1] 
ta : Acceleration time [sec] 
JM : Moment of inertia of rotor [kgm2] 
JL : Load moment of inertia [kgm2] 
Vr : Motor speed at which the acceleration torque starts to decrease [min-1] 
ks : Position loop gain =30 [s-1] 
η : Machine tool efficiency 
e : Base of a natural logarithm (≈ 2.71)

[Example of calculation for condition 4-1] Example of calculation 
The linear acceleration/deceleration is considered under the following condition. 
  Vm= 3000 [min-1] 
  ta = 0.07 [s] 
  ks =30 [s-1] 
  JL = 0.01412 [kgm2] 
Select the αiS22/4000-D provisionally selected in example of calculation 2.

[s] 
  ks =30 [s-1] 
  JL = 0.01412 [kgm2] 
Select the αiS22/4000-D provisionally selected in example of calculation 2. 
Since the moment of inertia of rotor JM is 0.0053 [kgm2] for αiS22/4000-D, Ta and Vr are as follows. 
  Ta = 3000×(2π/60)×(1/0.07)×(0.0053+0.01412÷0.9)×(1-e-30×0.07) 
   =82.7[Nm]=844[kgfcm] 
  Vr = 3000×{1-1/(0.07×30)×(1-e-30×0.07)}=1746[min-1]
```

---

## 第 221 頁
**本頁字數:** 844 字

### 內容摘要:
```text
Motor selection 
207 
Acceleration torque in bell acceleration/deceleration

The bell acceleration/deceleration acceleration torque assumes feed forward coefficient =1 (100%). The acceleration 
torque Ta, speed Vr, and maximum workpiece acceleration Acca are given below:

Ta : Acceleration torque [Nm] 
Vm : Motor speed in rapid traverse [min-1] 
t1 : Acceleration/deceleration time constant T1 [s] 
t2 : Acceleration/deceleration time constant T2 [s] 
JM : Moment of inertia of rotor [kgm2] 
JL : Load moment of inertia [kgm2] 
η : Machine tool efficiency 
Vr : Motor speed at which the acceleration torque starts to decrease [min-1] 
Acca : Maximum workpiece acceleration [m/s2] = [G] 
P : Pitch [m/rev]

NOTE 
Configure the value so that it will be t1 ≥ t2.

] = [G] 
P : Pitch [m/rev]

NOTE 
Configure the value so that it will be t1 ≥ t2.
```

---

## 第 222 頁
**本頁字數:** 800 字

### 內容摘要:
```text
208 
(2) Calculating the torque required by the motor shaft in acceleration 
To obtain the torque required by the motor shaft (T), add the steady-state load torque Tm to the acceleration torque 
Ta. (Cutting torque shall be Tcf=0)

T : Torque required by the motor axis 
Ta : Acceleration torque 
Tm : Steady-state load torque

[Example of calculation for condition 4-2] Acceleration torque 
Based on the example of calculation for condition 1, Tm= 3.0[Nm], and based on the example of calculation for 
condition 4‐1, Ta= 82.7[Nm], resulting in 
  T = 82.7[Nm] + 3.0[Nm] = 85.7[Nm] 
The speed when the maximum torque is required Vr is 1746 [min-1].

The speed torque characteristics of the αiS 22/4000-D, given below, show that the torque 85.7[Nm] and 1746[min-1] is 
beyond the intermittent operatin
```

---

## 第 222 頁
**本頁字數:** 796 字

### 內容摘要:
```text
cs of the αiS 22/4000-D, given below, show that the torque 85.7[Nm] and 1746[min-1] is 
beyond the intermittent operating zone of αiS 22/4000-D (insufficient torque).

If the desired shaft specification such as increasing acceleration time cannot be changed, it is necessary to increase 
the motor size. 
Select the αiS 30/4000-D (moment of inertia of rotor JM=0.0076[kgm2], 1.9 times load moment of inertia ratio) and 
calculate the acceleration torque again. 
 Ta=91.7[Nm]=936[kgfcm] 
 Vr=1746[min-1] 
 T=91.7[Nm]+3.0[Nm] = 94.7[Nm]

The speed torque characteristics of the αiS 30/4000-D, given below, show that the torque 94.7[Nm] and 1746[min-1] is 
within the intermittent operating zone of αiS 30/4000-D (acceleration is possible).

erating zone of αiS 30/4000-D (acceleration is possible).
```

---

## 第 223 頁
**本頁字數:** 777 字

### 內容摘要:
```text
Motor selection 
209 
2.2.5. 
Calculating the root-mean-square value of the torques 
A motor gets hot in proportion to the square of the torque. For a servo motor for which the load condition always 
changes, the calculated root-mean-square value of torque in a cycle must be sufficiently greater than the continuous 
torque (at low speed) Tc.

Root-mean-square value of torque in acceleration/deceleration in rapid traverse 
First, generate an operation pattern which performs acceleration/deceleration in rapid traverse with a desired 
frequency of positioning in rapid traverse. Write the time-speed graph and time-torque graph as shown below.

From the time-torque graph, obtain the root-mean-square value of torques applied to the motor during the single 
operation cycle.
```

---

## 第 223 頁
**本頁字數:** 800 字

### 內容摘要:
```text
time-torque graph, obtain the root-mean-square value of torques applied to the motor during the single 
operation cycle. Check whether the value is smaller than or equal to the continuous torque (at low speed) Tc.

Ta : Acceleration torque 
Tm : Steady-state load torque 
T0 : Torque when stopped 
When Trms falls within 90% of the continuous torque (at low speed) Tc, the servo motor can be used. 
(The entire thermal efficiency and other margins must be considered.)

NOTE 
In the above example, the determination is made based on the continuous torque (at low speed) Tc based on the 
assumption that the motor is being operated at high speed for a comparatively small proportion of the time.

[Example of calculation for condition 5-1] Root-mean-square value of the torques 
αiS 30/4000-D ( Tc = 3
```

---

## 第 223 頁
**本頁字數:** 755 字

### 內容摘要:
```text
n of the time.

[Example of calculation for condition 5-1] Root-mean-square value of the torques 
αiS 30/4000-D ( Tc = 30[Nm] = 306[kgfcm] ), Ta = 91.7[Nm], 
Tm = T0 = 3.0[Nm], t1 = 0.07[s], t2 = 2.0[s], t3 = 3.0[s]

= 15.4[Nm] < Tc×0.9 = 30×0.9 = 27[Nm] 
Therefore, operation is possible with αiS 30/4000-D.

Root-mean-square value of torque in a cycle in which the load varies 
If the load conditions (cutting load, acceleration/deceleration conditions, etc.) vary widely in a single cycle, write a 
time-torque graph according to the operation pattern, as in above item. Obtain the root-mean-square value of the 
torques and check that the value is smaller than or equal to the continuous torque (at low speed) Tc.

continuous torque (at low speed) Tc.
```

---

## 第 224 頁
**本頁字數:** 732 字

### 內容摘要:
```text
NOTE 
In the above example, the determination is made based on the continuous torque (at low speed) Tc based on the 
assumption that the motor is being operated at high speed for a comparatively small proportion of the time.

When the motor is being operated at high speed for a comparatively large proportion of the time 
Generally, a servo motor is being operated at high speed for a comparatively small proportion of the time, so 
comparison with the continuous torque (at low speed) is all that is needed. However, when a servo motor is being 
operated at high speed for a comparatively large proportion of the time, the impact caused when the continuous 
operating zone lowers as the speed increases must be taken into account.
```

---

## 第 224 頁
**本頁字數:** 804 字

### 內容摘要:
```text
he time, the impact caused when the continuous 
operating zone lowers as the speed increases must be taken into account. A simplified way to achieve this is to 
obtain the root-mean-square value of speed of the motor in a single cycle from the time-speed graph and check that 
the obtained root-means-square value of torque is less than or equal to 90% of the continuous operating zone based 
on the root-mean-square value of speed.

［Example of calculation for condition 5‐2］Root-mean-square value of the torque and root-
mean-square value of speed 
αiS 4/5000-D ( Tc = 4[Nm] = 41[kgfcm] ), Ta0 = 4[Nm], Ta1 = 3[Nm], Tm = 0.7[Nm], T0 = -0.2[Nm], 
t1 = 0.16[s], t2 = 0.5[s], t3 = 0.2[s], t4 = 0.14[s], t5 = 0.25[s], t6 = 0.15[s], t0 = 1.7[s]

0.2[s], t4 = 0.14[s], t5 = 0.25[s], t6 = 0.15[s], t0 = 1.7[s]
```

---

## 第 225 頁
**本頁字數:** 720 字

### 內容摘要:
```text
Since the root-mean-square value of torque is less than or equal to 90% of the continuous operating zone based on 
the root-mean-square value of speed, the αiS 4/5000-D can be used for operation. 
2.2.6. 
Calculating the percentage duty cycle and ON time with the maximum 
cutting torque 
Confirm that the time (duty percentage and ON time) during which the maximum cutting torque can be applied for 
cutting is shorter than the desired cutting time. 
First, calculate the load torque Tms applied when the cutting thrust Fc is applied to the motor shaft, and if it is smaller 
than the value obtained by multiplying continuous torque of motor (at low speed) Tc by heat efficiency a, continuous 
cutting can be performed.
```

---

## 第 225 頁
**本頁字數:** 471 字

### 內容摘要:
```text
by multiplying continuous torque of motor (at low speed) Tc by heat efficiency a, continuous 
cutting can be performed. 
If the value is greater than the product, follow the procedure below to calculate the ON time during which the 
maximum cutting load torque Tms can be applied to the motor (tON) and the ratio (ratio duty cycle with the maximum 
cutting torque) of the ON time to the total time of a single cutting cycle (t). Thermal efficiency α is assumed to be 0.9.
```

---

## 第 225 頁
**本頁字數:** 885 字

### 內容摘要:
```text
tting torque) of the ON time to the total time of a single cutting cycle (t). Thermal efficiency α is assumed to be 0.9. 
Calculate the percentage considering the specifications of the machine.

Judgment on availability of continuous operation at maximum cutting torque 
Calculate the percentage duty cycle according to the following figure and expressions.

[Example of calculation for condition 6-1] Percentage duty cycle and ON time with the maximum 
cutting torque 
The load torque in cutting is calculated as follows: 
F=Fc+μ(W+Fg+Fcf) 
F = 4900 + 0.05 × (11760 + 490 + 294) = 5527 [N] = 564 [kgf] 
Tm=(5527×20×10-3×1)/(2×π×0.9)+0.8=20.3[Nm]=208[kgfcm]

The continuous torque (at low speed) of the αiS30/4000-D Tc is 30 [Nm] = 306 [kgfcm]. 
Tc×a= 30×0.9 = 27[Nm]＞Tms = 20.3[Nm]

(at low speed) of the αiS30/4000-D Tc is 30 [Nm] = 306 [kgfcm]. 
Tc×a= 30×0.9 = 27[Nm]＞Tms = 20.3[Nm]
```

---

## 第 226 頁
**本頁字數:** 1216 字

### 內容摘要:
```text
Therefore, cutting can be performed continually.

Calculating the percentage duty cycle with the maximum cutting torque

If the load torque Tms becomes larger than the product of the motor continuous torque (at low speed) Tc and thermal 
efficiency (α), calculate the root-mean-square value of torque applied in a single cutting cycle. Specify tON and tOFF so 
that the value does not exceed the [continuous torque of motor (at low speed) Tc× heat efficiency a]. Then, calculate 
the percentage duty cycle with the maximum cutting torque as shown below.

[Example of calculation for condition 6-2] Percentage duty cycle and ON time with the maximum 
cutting force 
Assume that Tms is 40 [Nm] (Tm is 3.0 [Nm]).

The above ratio of the non-cutting time to the cutting time is required.

Assume that Tms is 40 [Nm] (Tm is 3.0 [Nm]).

The above ratio of the non-cutting time to the cutting time is required. The percentage duty cycle is calculated as 
follows:

Limitations on ON time 
The period during which continuous operation under an overload is allowed is also restricted by the OVC alarm level 
and overload duty characteristics. Refer to "I.3.1.1. About characteristics curves and data sheet(P.14)" for details.
```

---

## 第 227 頁
**本頁字數:** 772 字

### 內容摘要:
```text
Motor selection 
213 
2.2.7. 
Calculating the dynamic brake stop distance 
The equation for calculating the coasting distance when an abnormality occurs and the machine tool is stopped by 
dynamic braking with both ends of the motor power line shorted (dynamic brake stop distance) is given below:

JM : Moment of inertia of rotor [kgm2 ] [kgfcms2] 
JL : Load moment of inertia [kg⋅m2 ] [kgf⋅cms2] 
No : Motor speed at rapid traverse (min-1) 
L : Machine movement on one-rotation of motor [mm/rev] or [deg/rev] 
(No/60 × L = Vm) 
A : Coefficient A for calculating the dynamic brake stop distance 
B : Coefficient B for calculating the dynamic brake stop distance 
For details of A and B, see the table on the next item. 
For JM, see the data sheet of each motor in the "I.
```

---

## 第 227 頁
**本頁字數:** 836 字

### 內容摘要:
```text
p distance 
For details of A and B, see the table on the next item. 
For JM, see the data sheet of each motor in the "I. specifications(P.1)".

[Example of calculation for condition 7] Dynamic brake stop distance 
Desired stop distance = 150[mm] 
Coasting distance = (3000/60 × 20) [mm/s] × 0.05 [s] + (0.0076 [kgm2] + 0.01412 [kgm2]) 
×(3.7×10-2×3000[min-1]+3.4×10-9×30003[min-1])×20[mm/rev] 
= 138 [mm] 
Therefore, it is possible to stop within the desired stop distance. 
Finally, the αiS30/4000-D which satisfies selection conditions 1 to 7 is selected.

1. Use and calculate the "coefficients for dynamic brake calculation" to confirm whether the dynamic brake stop 
distance fits the desired stop distance. 
2. Applying the quick stop functions are recommended for shortening the stop distance at emergency stop or power 
failure.
```

---

## 第 227 頁
**本頁字數:** 871 字

### 內容摘要:
```text
Applying the quick stop functions are recommended for shortening the stop distance at emergency stop or power 
failure. 
Refer to ""AC SERVO MOTOR αi-B/αi/βi-B/βi series, LINEAR MOTOR LiS-B/LiS series, DD MOTOR DiS-B/DiS 
series PARAMETER MANUAL" (B-65270EN)" for details. 
To ensure the quick stop function works in the event of a power failure, maintain the control power supply (24 
VDC) for the CNC and servo amplifier by using an uninterruptible power supply (UPS) for example. 
3. If an alarm occurs, the quick stop function does not operate effectively and the stop distance will not be shortened. 
4. If you wish to use the quick stop function, it should be confirmed with an actual machine that the stop distance is 
shortened at an emergency stop or power failure.

h an actual machine that the stop distance is 
shortened at an emergency stop or power failure.
```

---

## 第 235 頁
**本頁字數:** 750 字

### 內容摘要:
```text
Motor selection 
221 
1. To protect the servo amplifier, ensure that the load inertia moment does not exceed the moment of inertia of rotor. 
When dynamic brake is applied exceeding the above range, the inside of the servo amplifier may be heated 
abnormally, leading to burning of the servo amplifier. Be sure to calculate the load moment of inertia correctly. 
If the servo amplifier is used exceeding the above range, please contact FANUC. 
2. If it is used at the load moment of inertia that exceeds five times of moment of inertia of rotor, when power failure 
(when quick stop function is disabled) or an alarm is generated during rapid traverse, set an interval of at least 30 
minutes before rebooting in order to protect the servo amplifier.
```

---

## 第 235 頁
**本頁字數:** 525 字

### 內容摘要:
```text
during rapid traverse, set an interval of at least 30 
minutes before rebooting in order to protect the servo amplifier. 
If suspension by dynamic brake is repeated continuously without intervals of 30 minutes or longer, the inside of the 
servo amplifier may be heated abnormally, leading to burning of the servo amplifier. 
3. If a speed command larger than the maximum rotation speed of the motor is erroneously input, the inside of the 
servo amplifier may be heated abnormally, leading to burning of the servo amplifier.
```

---

## 第 236 頁
**本頁字數:** 523 字

### 內容摘要:
```text
222 
2.3. 
About the servo motor selection data table 
Select a suitable motor according to load conditions, rapid traverse rate, increment system and other factors. To aid 
in selecting the correct motor, we recommend filling in the [Servo motor selection data table] on the following page. 
This section describes the servo motor selection data table. 
2.3.1. 
Servo motor selection data table 
The following describes the servo motor selection data table. There are sheets for SI unit and gravitational system of 
units.
```

---

## 第 237 頁
**本頁字數:** 883 字

### 內容摘要:
```text
Motor selection 
223 
Servo motor selection data table (SI unit) 
Machine-tool 
builder name

Specifications of moving object

* Weight of moving object (including workpiece, 
etc.)

* Moving direction (horizontal, vertical, rotation, 
slant)

* Support method (roll, slip, static pressure)

* Ball screw 
Ball screw diameter 
mm

* Rack & pinion 
Pinion diameter 
mm

Movement per rotation of motor

* Total load moment of inertia applied to the motor 
shaft (*1)

* Steady-state load torque (*2)

* Thrust counterforce by cutting

Required percentage duty cycle/ON time with the 
maximum cutting torque

Acceleration/deceleration time constant at rapid 
traverse 
T1 
ms

Rapid traverse positioning frequency (continuous, 
intermittent)

Motor specifications and characteristics

Note: When using a unit other than those described above, describe numeric values including the unit.
```

---

## 第 237 頁
**本頁字數:** 787 字

### 內容摘要:
```text
d characteristics

Note: When using a unit other than those described above, describe numeric values including the unit. (In case of rotary axis: mm → deg) 
* A numeric value required for selecting a motor. Be sure to enter data in this row. 
* Describe the total load moment of inertia when possible. If you enter the moment of inertia of coupling, reducer, and pulley (converted for motor axis), in the case of linear axis, it is also possible to calculate the total load moment of inertia in which the weight of moving 
object and ball screw is added by theoretical calculation. Be sure to describe the rotary axis because it cannot be calculated by theory. 
*2 The steady-state load torque indicates the steady-state component (gravity axis includes brake torque) per motor rotation.
```

---

## 第 237 頁
**本頁字數:** 569 字

### 內容摘要:
```text
e steady-state load torque indicates the steady-state component (gravity axis includes brake torque) per motor rotation. We would like you to provide as much information as possible, but if details are unknown, use a value theoretically calculated based on the 
weight and friction coefficient. As for the rotary axis, be sure to describe it in the same way as load moment of inertia. Do not include any torque required for acceleration/deceleration in this item. 
*3 for the positioning time, it is necessary to consider time for delay/setting of servo. 
(**) Comments
```

---

## 第 238 頁
**本頁字數:** 888 字

### 內容摘要:
```text
224 
Servo motor selection data table (gravitational system of units) 
Machine-tool 
builder name

Specifications of moving object

* Weight of moving object (including workpiece, 
etc.)

* Moving direction (horizontal, vertical, rotation, 
slant)

* Support method (roll, slip, static pressure)

* Ball screw 
Ball screw diameter 
mm

* Rack & pinion 
Pinion diameter 
mm

Movement per rotation of motor

* Total load moment of inertia applied to the motor 
shaft (*1)

* Steady-state load torque (*2)

* Thrust counterforce by cutting

Required percentage duty cycle/ON time with the 
maximum cutting torque

Acceleration/deceleration time constant at rapid 
traverse 
T1 
ms

Rapid traverse positioning frequency (continuous, 
intermittent)

Motor specifications and characteristics

Note: When using a unit other than those described above, describe numeric values including the unit.
```

---

## 第 238 頁
**本頁字數:** 787 字

### 內容摘要:
```text
d characteristics

Note: When using a unit other than those described above, describe numeric values including the unit. (In case of rotary axis: mm → deg) 
* A numeric value required for selecting a motor. Be sure to enter data in this row. 
* Describe the total load moment of inertia when possible. If you enter the moment of inertia of coupling, reducer, and pulley (converted for motor axis), in the case of linear axis, it is also possible to calculate the total load moment of inertia in which the weight of moving 
object and ball screw is added by theoretical calculation. Be sure to describe the rotary axis because it cannot be calculated by theory. 
*2 The steady-state load torque indicates the steady-state component (gravity axis includes brake torque) per motor rotation.
```

---

## 第 238 頁
**本頁字數:** 569 字

### 內容摘要:
```text
e steady-state load torque indicates the steady-state component (gravity axis includes brake torque) per motor rotation. We would like you to provide as much information as possible, but if details are unknown, use a value theoretically calculated based on the 
weight and friction coefficient. As for the rotary axis, be sure to describe it in the same way as load moment of inertia. Do not include any torque required for acceleration/deceleration in this item. 
*3 for the positioning time, it is necessary to consider time for delay/setting of servo. 
(**) Comments
```

---

## 第 239 頁
**本頁字數:** 789 字

### 內容摘要:
```text
Motor selection 
225 
2.3.2. 
Explanation of items 
(1) Title 
Machine-tool builder name 
Fill in this blank with the name of the user.

Kind of machine tool 
Describe the kind of machine. (lathe, miller, vertical/horizontal machining center)

Machine name 
Describe the machine name.

CNC model name 
Fill in this blank with the model name of CNC employed.

Spindle motor 
Enter the specifications and output of the spindle motor. (This item is needed when selecting Power Supply.)

Axis 
Fill in this blank with names of axes practically employed in CNC command. If the number of axes exceeds 4 axes, 
enter them in the second sheet.

(2) Specifications of moving object 
Data entered here is needed for determining the approximate motor load conditions (moment of inertia, load torque).
```

---

## 第 239 頁
**本頁字數:** 532 字

### 內容摘要:
```text
ect 
Data entered here is needed for determining the approximate motor load conditions (moment of inertia, load torque). 
Be sure to enter data in this row.

Weight (mass) of driven parts 
Enter the mass (weight) of driven parts, such as table, tool post, etc. by the maximum value including the weight of 
workpiece, jig, and so on. Do not include the weight of the counter balance.

Axis movement direction 
Enter horizontal, vertical, slant, or rotation as the movement directions of driven parts such as the table and tool post.
```

---

## 第 239 頁
**本頁字數:** 1041 字

### 內容摘要:
```text
ter horizontal, vertical, slant, or rotation as the movement directions of driven parts such as the table and tool post. 
Be sure to enter data because the axis movement direction is required for calculating the steady-state load torque 
and regenerative energy.

Slant angle 
Enter the angle which the movement direction forms with a horizontal surface only when the movement direction 
slants upward.

Counter balance 
Enter the weight of the counter balance in the vertical axis, if provided. 
Enter whether the counter balance is made by a weight or a force such as hydraulic force as this influences moment 
of inertia.

Supporting method 
Describe the type of sliding surface. (roll, slip, static pressure) 
Enter a special slide way material like Turcite, if used. 
Also enter the friction coefficient value.

static pressure) 
Enter a special slide way material like Turcite, if used. 
Also enter the friction coefficient value. This item is significant in estimating the friction coefficient for calculating 
mainly the load torque.
```

---

## 第 240 頁
**本頁字數:** 784 字

### 內容摘要:
```text
226 
Ball screw 
For a ball screw, enter the diameter, pitch, and length in order. If a rack and pinion or other mechanism is used, also 
enter the traveling distance of the machine tool per revolution of the pinion.

Rack & pinion 
For a rack and pinion, enter the diameter and thickness of the pinion.

Friction coefficient 
Enter the friction coefficient of the target axis.

Machine efficiency 
This value is used for calculating the transfer efficiency of motor output on a machine tool. Standard value is 0.9. 
Generally, a drop in transfer efficiency below 0.9 is expected if a reduction gear having a large reduction ratio is used. 
Be sure to enter data in this row after verification.

Reduction ratio 
Enter the total reduction ratio between the ball screw and servo motor.
```

---

## 第 240 頁
**本頁字數:** 873 字

### 內容摘要:
```text
n this row after verification.

Reduction ratio 
Enter the total reduction ratio between the ball screw and servo motor. 
For the rack pinion, enter the total reduction ratio between the final stage pinion and servo motor, and for the rotary 
table, enter the total gear ratio between the table and servo motor.

(3) Mechanical specifications 
Enter basic data that is required for selecting the motor. 
For details on how to calculate each of the items, see "II.2.2. Selecting a motor(P.201)".

Movement per rotation of motor 
Enter the movement of the machine tool when the motor rotates one turn. 
Example) 
 
When the pitch of ball screw is 12 [mm] and the reduction ratio is 2/3, 
12 [mm] × 2/3 = 8 [mm] 
 
When the reduction ratio is 1/72 in rotary table ; 
360 [deg.] × 1/72 = 5 [deg.]

Least input increment of CNC 
Enter the least input increment of CNC command.
```

---

## 第 240 頁
**本頁字數:** 1255 字

### 內容摘要:
```text
ary table ; 
360 [deg.] × 1/72 = 5 [deg.]

Least input increment of CNC 
Enter the least input increment of CNC command. (The standard value is 0.001 [mm].)

Rapid traverse rate 
Enter the rapid traverse rate required for machine tool specifications.

Motor speed in rapid traverse 
Enter the rotation speed during rapid traverse.

Total load moment of inertia applied to the motor shaft 
Enter a load moment of inertia applied by the moving object reflected on the motor shaft. While this includes the 
moment of inertia of the workpiece, ball screw, coupling, etc., the rotor moment of inertia of the motor is not included. 
Refer to "II.2.2.3. Calculating the load moment of inertia(P.203)" for details of the calculation method. 
In the case of a linear axis, you can have the load moment of inertia obtained by theoretical calculation of "Other 
moment of inertia".

linear axis, you can have the load moment of inertia obtained by theoretical calculation of "Other 
moment of inertia". In the case of a rotary axis, however, be sure to enter the load moment of inertia because it 
cannot be obtained by theoretical calculation. Entering two significant digits past the decimal point as the moment of 
inertia is sufficient. 
(Example: 0.2865 → 0.29)
```

---

## 第 241 頁
**本頁字數:** 827 字

### 內容摘要:
```text
Motor selection 
227 
Other moment of inertia 
Enter the load moment of inertia of the coupling and other transmission mechanisms; this does not include the load 
moment of inertia of the weight of the moving object and the ball screw. Entering two significant digits past the 
decimal point as the moment of inertia is sufficient. (Example: 0.2865 → 0.29)

Steady-state load torque 
Enter the torque obtained by calculating the force applied for moving the machine tool and steady-state components 
such as friction (including holding torque in the case of a gravity shaft) reflected on the motor shaft when it is rotating 
at a fixed speed. (It is not necessary to describe the torque required for acceleration/deceleration.) If details are 
unknown, use a value calculated logically from the weight and friction coefficient.
```

---

## 第 241 頁
**本頁字數:** 679 字

### 內容摘要:
```text
ation/deceleration.) If details are 
unknown, use a value calculated logically from the weight and friction coefficient. Enter the steady-state load torque 
of the rotary axis in the same way as for the total load moment of inertia as it cannot be calculated logically. 
If the load torque values differ during lifting and lowering in the vertical axis, enter both values. Also, if the load torque 
values differ during rapid traverse and cutting feed, enter a notice to that effect. 
Since torque produced in low speed without cutting may be applied even when the motor has stopped, a sufficient 
allowance is necessary as compared with the continuous rated torque of the motor.
```

---

## 第 241 頁
**本頁字數:** 685 字

### 內容摘要:
```text
n the motor has stopped, a sufficient 
allowance is necessary as compared with the continuous rated torque of the motor. Suppress this load torque so that 
it is lower than 70% of the continuous rated torque.

Thrust counterforce by cutting 
Describe the maximum thrust counterforce applied during cutting.

Maximum cutting torque 
Enter the torque value on the motor shaft corresponding to the maximum value of the above cutting thrust. When you 
enter this value, add the steady-state load to the motor shaft converted value for the cutting thrust. 
Since the torque transfer efficiency may substantially deteriorate to a large extent due to the counterforce from the 
slideway, etc.
```

---

## 第 241 頁
**本頁字數:** 718 字

### 內容摘要:
```text
que transfer efficiency may substantially deteriorate to a large extent due to the counterforce from the 
slideway, etc. produced by the cutting thrust, obtain an accurate value by taking measured values in similar machine 
tools and other data into account.

Required percentage duty cycle/ON time with the maximum cutting torque 
Enter the duty time and ON time with the maximum cutting torque in the above item applied.

Positioning distance 
Enter the distance as a condition required for calculating the rapid traverse positioning frequency. 
When an exclusive positioning device is used, enter this value together with the desired positioning time below.

Positioning time 
Describe the desired positioning time.
```

---

## 第 241 頁
**本頁字數:** 822 字

### 內容摘要:
```text
r this value together with the desired positioning time below.

Positioning time 
Describe the desired positioning time. 
When the device is actually attached on the machine tool, note that servo delay and setting times must also be taken 
into consideration in the positioning time.

In-position width 
Enter the in-position width set value as a condition required for calculating the positioning time. 
Note that the positioning time changes according to this value. 
Acceleration/deceleration time constant at rapid traverse 
Enter the desired acceleration/deceleration time constant in rapid traverse. 
The acceleration/deceleration time is determined according to the load moment of inertia, load torque, motor output 
torque, and working speed.

ment of inertia, load torque, motor output 
torque, and working speed.
```

---

## 第 242 頁
**本頁字數:** 844 字

### 內容摘要:
```text
228 
The acceleration/deceleration type during rapid traverse will be linear or bell type, and in the case of linear 
acceleration/deceleration, enter T1 only, and in the case of bell type acceleration/deceleration, enter T1 and T2.

When cutting feed is important, enter the time constant in cutting feed. The acceleration/deceleration mode during 
cutting feed is either linear or bell type.

Position loop gain 
Fill in this blank with a value which is considered to be settable judging it from the load moment of inertia value based 
on experiences. Since this value is not always applicable due to rigidity, damping constant, and other factors of the 
machine tool, it is usually determined on the actual machine tool.

Rapid traverse positioning frequency 
Enter the rapid traverse positioning frequency per minute as the number of times.
```

---

## 第 242 頁
**本頁字數:** 1063 字

### 內容摘要:
```text
Rapid traverse positioning frequency 
Enter the rapid traverse positioning frequency per minute as the number of times. Enter whether the value is for 
continuous positioning over a long period of time or for intermittent positioning within a fixed period of time. (This 
value is used to check the OVC alarm and whether the motor is overheated or not by a flowing current during 
acceleration/deceleration, or to check the regenerative capacity of the amplifier.)

Dynamic brake stop distance 
Enter the coasting distance when an abnormality occurs and the machine tool is stopped by dynamic braking with 
both ends of the motor power line shorted.

(4) Motor specifications and characteristics 
Motor name 
Enter the model name of the model, if desired.

Pulsecoder 
Enter the specification of Pul

characteristics 
Motor name 
Enter the model name of the model, if desired.

Pulsecoder 
Enter the specification of Pulsecoder, if desired.

Shaft shape 
Enter the shape of the motor shaft.

Brake (Yes/No) 
Enter whether or not the motor has an integrated brake.
```

---

## 第 243 頁
**本頁字數:** 445 字

### 內容摘要:
```text
Motor selection 
229 
2.4. 
Selecting the αiPS 
When selecting the αiPS, use the values shown in "Data for selecting the αiPS" as they are in the equation for the 
selection of the αiPS. For details about the selection method, refer to "SERVO AMPLIFIER αi-D series 
DESCRIPTIONS" (B-65552EN) "Selecting the αiPS-D". 
For "Data for selecting the αiPS", a table is described in the appendix of this manual "A. Data for selecting the 
αiPS(P.251)".
```

---

## 第 247 頁
**本頁字數:** 888 字

### 內容摘要:
```text
Handling of the servo motor 
233 
1. 
Handling of the servo motor

1.1. 
Checking a delivered servo motor and storing a servo motor 
When the servo motor is delivered, check the following items. 
 
Is the motor according to the specification (model, shaft, detector specifications) 
 
Damage caused by the transportation. 
 
The shaft is normal when rotated by hand. 
 
The brake works. 
 
Are there any loose screws or screws with clearance? 
FANUC servo motors are completely checked before shipment, and the inspection at acceptance is normally 
unnecessary. When an inspection is required, check the specifications (wiring, current, voltage, etc.) of the motor and 
sensor. 
Store the motor indoors. The storage temperature is 0°C to 40°C. 
Do not store the motor in places listed below as the motor may be damaged or rust. 
 
Place with high humidity so condensation will form.
```

---

## 第 247 頁
**本頁字數:** 730 字

### 內容摘要:
```text
otor in places listed below as the motor may be damaged or rust. 
 
Place with high humidity so condensation will form. 
 
Place with extreme temperature changes. 
 
Place always exposed to vibration. (The bearing may be damaged. ) 
 
Place with much dust. 
In case of long-term storage, apply antirust oil on the machining surface of shafts and other parts regardless of 
storage conditions. 
1.2. 
Separating and disposing of a servo motor 
For a servo motor, a plastic part is used. 
Disassemble the motor as shown in the following figure, separate the plastic part (Pulsecoder cover), and dispose of 
the motor. The following plastic material is used: 
Plastic material : > (PBT+PC)-GF(30)FR(17)<

> (PBT+PC)-GF(30)FR(17)<
```

---

## 第 248 頁
**本頁字數:** 845 字

### 內容摘要:
```text
234 
2. 
Mounting a servo motor

2.1. 
Methods for coupling the shaft 
In many cases, the following four methods are used for coupling the motor shaft to the ball screw on a machine: 
Direct connection through a flexible coupling, direct connection through a rigid coupling, connection through gears, 
and connection through timing belts. It is important to understand the characteristics of each method, and select one 
that is most suitable for the machine.

Direct connection using a flexible coupling 
Direct connection by a flexible coupling has the following advantages over connection using gears: 
 
Even if the angle of the motor shaft to the ball screw changes, it can be compensated to a certain extent. 
 
Because a flexible coupling connects elements with less backlash, driving noise from joints can be significantly 
suppressed.
```

---

## 第 248 頁
**本頁字數:** 642 字

### 內容摘要:
```text
se a flexible coupling connects elements with less backlash, driving noise from joints can be significantly 
suppressed. 
However, this method has the following disadvantages: 
 
The motor shaft and the ball screw must not slide from each other in the radial direction (for single coupling). 
 
Loose assembly may result in lower rigidity. 
When the motor shaft needs to be connected directly to the ball screw, connecting them using a flexible coupling 
facilitates adjustment and installation of the motor. 
To use a single coupling, the machine needs to be designed so that the centers of the motor shaft and the ball screw 
are aligned.
```

---

## 第 248 頁
**本頁字數:** 892 字

### 內容摘要:
```text
ingle coupling, the machine needs to be designed so that the centers of the motor shaft and the ball screw 
are aligned. (In the same way as with a rigid coupling, the use of a single coupling demands that there be almost no 
relative eccentricity between the axes.) 
If it is difficult to align the centers, a double coupling needs to be employed.

Direct connection using a rigid coupling 
Direct connection using a rigid coupling has the following advantages over direct connection using a flexible coupling: 
 
More economical 
 
The coupling rigidity can be increased. 
 
If the rigidity is the same as with a flexible coupling, the moment of inertia can be reduced. 
However, this method has the following disadvantages: 
 
The motor shaft and the ball screw must not slide from each other in the radial direction. 
 
The angle of the motor shaft to the ball screw must not change.
```

---

## 第 248 頁
**本頁字數:** 679 字

### 內容摘要:
```text
t not slide from each other in the radial direction. 
 
The angle of the motor shaft to the ball screw must not change. 
For this reason, a rigid coupling needs to be mounted very carefully. 
It is desirable that the run-out of the ball screw is 0.01 mm or less for machine tools. When a rigid coupling is used on 
the motor shaft, the run-out of the hole for the ball screw must be set to 0.01 mm or less by adjusting the tightness of 
the locking element. 
The run-out of the motor shaft and the ball screw in the radial direction can be adjusted or compensated to a certain 
extent by deflection. Note, however, that it is difficult to adjust or measure changes in the angle.
```

---

## 第 248 頁
**本頁字數:** 1045 字

### 內容摘要:
```text
sated to a certain 
extent by deflection. Note, however, that it is difficult to adjust or measure changes in the angle. Therefore, the 
structure of the machine should be such that accuracy can be fully guaranteed.

Gears 
This method is used when the motor cannot be put in line with the ball screw because of the mechanical interference 
problem or when the reduction gear is required in order to obtain large torque. 
The following attention should be paid to the gear coupling method: 
 
Grinding finish should be given to the gear, and eccentricity, pitch error, tooth-shape deviations etc. should be 
reduced as much as possible. Please use the JIS, First Class as a reference of accuracy. 
 
Adjustment of backlash should be carefully performed.

e. Please use the JIS, First Class as a reference of accuracy. 
 
Adjustment of backlash should be carefully performed. Generally, if there is too little backlash, a high-pitched 
noise will occur during high-speed operation, and if the backlash is too big, a drumming sound of the tooth
```

---

## 第 249 頁
**本頁字數:** 791 字

### 內容摘要:
```text
Mounting a servo motor 
235 
surfaces will occur during acceleration/deceleration. Since these noises are sensitive to the amount of backlash, 
the structure should be so that adjustment of backlash is possible at construction time.

Timing belt 
A timing belt is used in the same cases as gear connection, but in comparison, it has advantages such as low cost 
and reduced noise during operation, etc. However, it is necessary to correctly understand the characteristics of timing 
belts and use them appropriately to maintain high accuracy. 
Generally, the rigidity of timing belt is sufficiently higher than that of other mechanical parts such as ball screw or 
bearing, so there is no danger of inferiority of performance of control caused by reduction of rigidity by using timing 
belt.
```

---

## 第 249 頁
**本頁字數:** 997 字

### 內容摘要:
```text
g, so there is no danger of inferiority of performance of control caused by reduction of rigidity by using timing 
belt. When using a timing belt with a position sensor on the motor shaft, there are cases where poor accuracy caused 
by backlash of the belt tooth and pulley tooth, or elongation of belt after a long time becomes a problem, so 
consideration should be given to whether these errors significantly affect accuracy. In case the position sensor is 
mounted behind the timing belt (for example, on the ball screw axis), a problem of accuracy does not occur. 
Life of the timing belt largely varies according to mounting accuracy and tension adjustment. Please refer to the 
manufacturer's Instruction Manual for correct use. 
When using a timing belt, be careful about the radial load. Refer to "III.2.3.

er's Instruction Manual for correct use. 
When using a timing belt, be careful about the radial load. Refer to "III.2.3. Allowable axis load for a servo motor(P.237)" 
for details.
```

---

## 第 250 頁
**本頁字數:** 867 字

### 內容摘要:
```text
236 
2.2. 
Fastening the shaft 
Taper shaft 
In case of taper shafts, the load must be exerted on the tapered surface. 
For this reason, at least 70% of gage fitting is required on the tapered surface. 
In addition, the screw at the end of the taper shaft must be properly tightened to achieve sufficient axial force.

Recommended tightening torque 
 
M6 × 1 φ11 taper shaft 3 to 3.2 Nm 
 
M8 x1 φ14 taper shaft 7 to 8Nm 
 
M10 x1.25 φ16 taper shaft 15 to 16Nm 
 
M12 x1.25 φ24 taper shaft 20 to 25Nm 
 
M20 x1.5 φ32 taper shaft 60 to 120Nm 
 
M24 x2 φ38 taper shaft 160 to 200Nm

Straight shaft 
To use a straight shaft that has no key way, connect the shaft with a coupling using a locking element. 
Because the locking element connects elements by the friction generated when the screw is tightened, it is free from 
backlash and the concentration of stress.
```

---

## 第 250 頁
**本頁字數:** 768 字

### 內容摘要:
```text
ements by the friction generated when the screw is tightened, it is free from 
backlash and the concentration of stress. For this reason, the locking element is highly reliable for connecting 
elements. 
To assure sufficient transmission with the locking element, factors such as the tightening torque of the screw, the size 
of the screw, the number of screws, the clamping flange, and the rigidity of connecting elements are important. Refer 
to the manufacturer's specifications before using the locking element. 
When a coupling or gear is mounted using the locking element, tighten the screws to remove a run-out of the coupling 
or gear including the shaft.

Straight shaft with a key groove 
In a straight shaft with a key way, torque is transmitted at the key.
```

---

## 第 250 頁
**本頁字數:** 580 字

### 內容摘要:
```text
ding the shaft.

Straight shaft with a key groove 
In a straight shaft with a key way, torque is transmitted at the key. 
This means that if there is a looseness between the key and key way, the impact incurred at the time of inversion 
increases, which can result in shaft breakage, or a backlash occurs as a result of the looseness, which can lower 
positioning accuracy. Therefore, the key and key way should be designed so as to minimize the looseness between 
them. 
When performing acceleration abruptly or frequently, select a taper shaft or straight shaft with no key way.
```

---

## 第 251 頁
**本頁字數:** 874 字

### 內容摘要:
```text
Mounting a servo motor 
237 
2.3. 
Allowable axis load for a servo motor 
The allowable axis load for the shaft of each motor is indicated in "I.3.2. Outline drawings(P.117)." Using a motor under 
a load higher than the allowable axial load may break the motor. When designing a machine and connecting a motor 
to the machine, fully consider the following points: 
 
The allowable radial load is determined, assuming that a radial load is applied to the end of the shaft. 
 
Applying a load higher than the allowable axis load may break the bearing. Applying a radial load higher than the 
allowable radial load may break the shaft due to a fatigue failure. 
 
A radial load indicates the constant force continuously applied to the shaft depending on the mounting method 
(such as belt tension) and the force by the load torque (such as dividing moment by pulley radius).
```

---

## 第 251 頁
**本頁字數:** 866 字

### 內容摘要:
```text
the mounting method 
(such as belt tension) and the force by the load torque (such as dividing moment by pulley radius). 
 
When a timing belt is used, the belt tension is critical particularly. Too tight a belt causes a fault such as the 
broken shaft. Belt tension must be controlled so as not to exceed the limits calculated from the allowable radial 
load. Positioning the pulley as close to the bearing as possible in design can prevent possible faults such as the 
broken shaft. 
 
In some use conditions, the pulley diameter and gear size should be considered. For example, when the αiF 
4/5000-D model is used with a gear and pulley with a radius of 2.5 cm or less, the radial load with a torque of 18 
Nm (184 kgf⋅cm) exceeds the allowable axis load, 686 N (70 kgf). In this case, take measures such as 
supporting the end of the motor shaft mechanically.
```

---

## 第 251 頁
**本頁字數:** 1094 字

### 內容摘要:
```text
able axis load, 686 N (70 kgf). In this case, take measures such as 
supporting the end of the motor shaft mechanically. 
 
Since the standard single-row deep-groove ball bearing is used for the motor bearing, too high an axial load 
cannot be used. To use a worm or helical gear, in particular, use another bearing. 
 
The motor bearing is generally fixed with a C-snap ring, and there is a small play in the axial direction. If the axial 
play affects the positioning in the case of using a worm or helical gear, fit it with another bearing. 
2.4. 
Shaft run-out accuracy of a servo motor 
The shaft run-out accuracy of each motor is described in "I.3.2. Outline drawings(P.117)".

ut accuracy of a servo motor 
The shaft run-out accuracy of each motor is described in "I.3.2. Outline drawings(P.117)". 
The methods of measuring the shaft run-out accuracy are specified below: 
Item 
Measuring method 
Shaft diameter run-out

Run-out against the shaft center of centering 
location 
(Only for flange type)

Run-out of the flange mounting surface to the 
shaft center 
(Only for flange type)
```

---

## 第 252 頁
**本頁字數:** 819 字

### 內容摘要:
```text
238 
2.5. 
Other notes on axis design 
Machine movement per 1 revolution of motor shaft 
The machine movement per 1 revolution of motor shaft must be determined at the first stage of machine design 
referring the load torque, load inertia moment, rapid traverse speed, and relation between minimum increment and 
resolution of the position sensor mounted on the motor shaft. To determine this amount, the following conditions 
should be taken into consideration. 
 
The machine movement per 1 revolution of motor shaft must be determined based on the specified maximum 
rotation speed so that the desired rapid traverse speed can be obtained. For example, if the motor's maximum 
rotation speed is 1500 min-1 and the rapid traverse speed must be 12 m/min., the machine movement per 1 rev. 
must be 8 mm/rev. or higher.
```

---

## 第 252 頁
**本頁字數:** 887 字

### 內容摘要:
```text
1500 min-1 and the rapid traverse speed must be 12 m/min., the machine movement per 1 rev. 
must be 8 mm/rev. or higher. 
 
As the machine movement per 1 revolution of motor shaft is reduced, both the load torque and the load inertia 
moment reflected to motor shaft also decrease. Therefore, to obtain large thrust, the machine movement per 1 
rev. should be the lowest value at which the desired rapid traverse speed can be obtained. 
 
Assuming that the accuracy of the reduction gear is ideal, it is advantageous to make the machine movement per 
1 rev. of motor shaft as low as possible to obtain the highest accuracy in mechanical servo operations. In addition, 
minimizing the machine movement per 1 rev. of motor shaft can increase the servo rigidity as seen from the 
machine's side, which can contribute to system accuracy and minimize the influence of external load changes.
```

---

## 第 252 頁
**本頁字數:** 799 字

### 內容摘要:
```text
n from the 
machine's side, which can contribute to system accuracy and minimize the influence of external load changes. 
 
When the machine is characterized by repeated acceleration/deceleration cycles, a heating problem may occur 
due to the current flow caused by the acceleration and deceleration. Should this occur, the machine travel 
distance per motor shaft revolution should be modified. Given optimum conditions, the machine travel distance 
per motor shaft revolution is set such that the motor's rotor inertia moment equals the load inertia moment based 
on motor shaft conversion 
For machines such as punch presses and PCB drilling machines, the machine's travel distance per motor shaft 
revolution should be set so as to satisfy this optimum condition as far as possible, while also
```

---

## 第 252 頁
**本頁字數:** 806 字

### 內容摘要:
```text
stance per motor shaft 
revolution should be set so as to satisfy this optimum condition as far as possible, while also considering the rapid 
traverse rate and increment system.

Precautions for using linear scale 
In the case where the machine moves in a linear direction and movement is directly detected by linear scale such as 
inductosyn, magne-scale etc., special considerations are necessary in comparison with the method where feedback 
is produced by detecting the motor shaft rotation. This is because the machine movement now directly influences the 
characteristics of the control system. 
The following block diagram shows feedback produced using a linear scale.

The response of this control system is determined by the adjustment value (position loop gain) of the position control 
circuit.
```

---

## 第 252 頁
**本頁字數:** 548 字

### 內容摘要:
```text
onse of this control system is determined by the adjustment value (position loop gain) of the position control 
circuit. In other words, the position loop gain is determined by the specified response time of the control system. 
On the other hand, unless the response time of the section detecting the position within the velocity control circuit 
(velocity loop: the section enclosed by the broken line in the figure above) is sufficiently shorter than the response 
time determined by the position loop gain, the system does not operate properly.
```

---

## 第 252 頁
**本頁字數:** 991 字

### 內容摘要:
```text
sufficiently shorter than the response 
time determined by the position loop gain, the system does not operate properly. In other words, when a command 
signal is put into point A, response time of the machine where position signals are detected must be sufficiently 
shorter than the response time defined by the position loop gain.

If the response of the sensor section is slow, the position loop gain should be reduced to have the system operate 
normally, and as a result, the response of the whole system becomes slow. The same problem is caused when 
moment of inertia is great. 
The main causes for slow response are the mass of the machine and the elastic deformation of the machine system.

great. 
The main causes for slow response are the mass of the machine and the elastic deformation of the machine system. 
As an index for estimating the response of this machine system, the natural frequency of the machine is used, and 
this is briefly calculated by the following equation.
```

---

## 第 253 頁
**本頁字數:** 718 字

### 內容摘要:
```text
Wm : Natural frequency 
JL : Load inertia moment reflected to motor shaft 
Km : Rigidity of machine system 
(= Torque necessary to elastically deform 1[rad] at the motor shaft when the machine table is clamped) 
These values can be obtained by calculating the elastic deformation for each section of the driving system. 
The machine should be designed so that the value of this natural frequency [Hz] will be more than or equal to the 
value of the position loop gain [s-1]. For example, when setting 20 [s-1] as the value of position loop gain, natural 
frequency of machine system must be more than 20 [Hz]. In this case, the response of the control system becomes a 
problem for extremely small amounts of movement.
```

---

## 第 253 頁
**本頁字數:** 643 字

### 內容摘要:
```text
an 20 [Hz]. In this case, the response of the control system becomes a 
problem for extremely small amounts of movement. Consequently, the natural frequency should be calculated from 
the rigidity at extremely small displacement such as 10 [μm] or less.

Stick slip 
If machine movement causes a stick slip, the control system does not operate normally. That is, it does not stop 
where it is supposed to, but a phenomenon occurs where it goes beyond and then back within an extremely small 
range (hunting). To avoid stick slip, the machine rigidity should be increased, or friction characteristics of the sliding 
surface should be improved.
```

---

## 第 253 頁
**本頁字數:** 1135 字

### 內容摘要:
```text
slip, the machine rigidity should be increased, or friction characteristics of the sliding 
surface should be improved. 
When the sliding surface friction characteristic is as in the figure below, stick slip occurs easily.

Value of machine overrun (Damping coefficient of machine system) 
When the machine is floated by static pressure, etc., there are cases where the machine keeps on moving within the 
range of backlash although the motor shaft has stopped. If this amount is large, hunching occurs as well. 
To avoid this, backlash should be reduced (especially the backlash of the element that moves last) and the 
appropriate damping should be considered.

Reciprocating motion over a short distance 
Continuing reciprocating motions over a short distance with a low revolution speed causes the bearing to become 
short of lubricant, which can shorten the life of the bearing.

with a low revolution speed causes the bearing to become 
short of lubricant, which can shorten the life of the bearing. When such motions are performed, special care should be 
taken by, for example, turning the motor at least one turn periodically.
```

---

## 第 254 頁
**本頁字數:** 900 字

### 內容摘要:
```text
240 
2.6. 
Cautions in mounting a servo motor 
The servo motor contains precision sensor, and is carefully machined and assembled to provide the required 
accuracy. Pay attention to the following items to maintain the accuracy and prevent damage to the sensor.

 
Secure the servo motor uniformly using four bolt holes provided on the front flange.

 
Ensure that the surface on which the machine is mounted is sufficiently flat. 
When mounting on the machine, take care not to apply a shock to the motor.

 
When it is unavoidable to tap the motor for adjusting the position, etc., use a plastic hammer and tap only the front 
flange if possible.

A precision sensor is directly connected to the servo motor shaft. Pay attention to the following items to prevent 
damage to the sensor.

ly connected to the servo motor shaft. Pay attention to the following items to prevent 
damage to the sensor.
```

---

## 第 255 頁
**本頁字數:** 607 字

### 內容摘要:
```text
Mounting a servo motor 
241 
 
When connecting the power transmission elements such as a gear, a pulley and a coupling to the shaft, take care 
not to apply a shock to the shaft.

 
Generally, in the case of a straight shaft, use a locking element for connection with the shaft. 
 
In the case of a tapered shaft, match the tapered surface with the power transmission element such as a pulley 
and fix it by tightening the screw at the end. 
When the woodruff key is too tight, don't tap it with a hammer. Use the woodruff key mainly for positioning, and 
use the tapered surface for torque transmission.
```

---

## 第 255 頁
**本頁字數:** 483 字

### 內容摘要:
```text
tap it with a hammer. Use the woodruff key mainly for positioning, and 
use the tapered surface for torque transmission. 
Machine the tapered surface of the power transmission element so that over 70% of the whole surface is 
contacted.

 
To remove the connected power transmission element, be sure to use a jig such as a gear puller.

 
When tapping slightly to remove the tightly contacted tapered surface, tap in the radial direction to prevent a 
shock in the axial direction.
```

---

## 第 256 頁
**本頁字數:** 1061 字

### 內容摘要:
```text
242 
 
Suppress the rotary unbalance of the connected power transmission element to the level as low as possible. It is 
usually believed that there is no problem in the symmetrical form. Be careful when rotating continuously the 
asymmetrical different form power transmission element. 
Even if the vibration caused by the unbalance is as small as 0.5G, it may damage the motor bearing or the 
sensor. 
 
An exclusive large oil seal is used in the flange of the motor. The oil seal surface is made of steel plate. Take care 
not to apply a force to the oil seal when installing the motor or connecting the power transmission elements.

 
Do not set up the αiS8-D or higher or αiF4-D or higher servo motor (whose flange size is at least 130 mm) with 
the Pulsecoder down.

p the αiS8-D or higher or αiF4-D or higher servo motor (whose flange size is at least 130 mm) with 
the Pulsecoder down. If you want to use the motor with the shaft directed upward, set up the motor so that its own 
weight is not applied to the Pulsecoder as shown in the figure below.
```

---

## 第 257 頁
**本頁字數:** 838 字

### 內容摘要:
```text
Use environment for servo motors 
243 
3. 
Use environment for servo motors

3.1. 
Ambient Temperature, Humidity, Installation Height, and Vibration 
Ambient temperature 
The ambient temperature should be 0°C to 40°C. If the ambient temperature exceeds this range, the operating 
conditions must be eased to prevent the motor and detector from overheating. 
(The specification values and external dimensions in the data sheet assume an ambient temperature of 20°C.)

Ambient humidity 
The ambient humidity should be 80%RH or less and no condensation should be caused.

Installation height 
At an altitude of up to 1,000 meters above the sea level, no particular attention is required. When operating the 
machine at a higher level, special care is unnecessary if the ambient temperature is lowered 1°C at every 100 m 
higher than 1,000 m.
```

---

## 第 257 頁
**本頁字數:** 559 字

### 內容摘要:
```text
higher level, special care is unnecessary if the ambient temperature is lowered 1°C at every 100 m 
higher than 1,000 m. For example, when the machine is installed at a place of 1,500 meters above sea level, there is 
no problem if the ambient temperature is 35°C or less.

Vibration 
When installed in a machine, the vibration applied to the motor must not exceed 5G.

If any one of the four environmental conditions (ambient temperature, ambient humidity, installation height, and 
vibration) specified above is not satisfied, the output must be restricted.
```

---

## 第 258 頁
**本頁字數:** 755 字

### 內容摘要:
```text
Use environment for servo motors

244 
3.2. 
Usage considering environmental resistance 
Overview 
The motor is an electric device, and if the lubricant or cutting fluid falls on the motor, it will enter the inside of the 
motor, possibly adversely affecting the motor. In particular, if the cutting fluid adheres to the motor, it will deteriorate 
the resin or rubber sealing members, causing a large amount of cutting fluid to enter the inside of the motor and 
possibly damaging the motor. When using the motor, note the points described below.

Motor protection class 
The motor protection class is IP67 of IEC60034-5 standard for the motor alone with the standard specification. 
(Except the fan motor and the connectors of models with a cooling fan.
```

---

## 第 258 頁
**本頁字數:** 790 字

### 內容摘要:
```text
the motor alone with the standard specification. 
(Except the fan motor and the connectors of models with a cooling fan. The connectors of Pulsecoders are waterproof 
when engaged.) 
The protection types mentioned above do not apply to the part that the motor axis penetrates. 
For a description of the water-proof properties of each connector, see the section on that connector. 
Note that IP67 satisfies the provisions for short-time water immersion, and do not guarantee their waterproof 
performance in an atmosphere in which the cutting fluid is applied directly to the motor.

Motor periphery 
If the cutting fluid or lubricant falls on the motor, it will adversely affect the sealing properties of the motor surface, 
entering the inside of the motor and possibly damaging the motor.
```

---

## 第 258 頁
**本頁字數:** 727 字

### 內容摘要:
```text
y affect the sealing properties of the motor surface, 
entering the inside of the motor and possibly damaging the motor. Note the following points on use: 
Make sure that the motor surface is never wet with the cutting fluid or lubricant, and also make sure that no fluid 
builds up around the motor. If there is a possibility of the surface being wet, a cover is required. Be sure to mount a 
cover even when using an IP67 type motor.

If the cutting fluid is misted, the cutting fluid may be condensed on the inside of the cover and fall on the motor. Make 
sure that no condensed droplets fall on the motor.

Completely separate the machining area from the motor area, using a telescopic cover, accordion curtain, and so on.
```

---

## 第 258 頁
**本頁字數:** 1105 字

### 內容摘要:
```text
or.

Completely separate the machining area from the motor area, using a telescopic cover, accordion curtain, and so on. 
Note that partitions such as accordion curtains are consumable and require periodic inspection for damage.

Output shaft seal (oil seal) 
For all models, the shaft of the servo motor is provided with an oil seal to prevent entry of oil and other fluids into the 
motor. It does not, however, completely prevent the entry of lubricant and other fluids depending on the working 
conditions. Note the following points on use: 
When the motor is rotating, the oil seal has an effect of discharging any oil that enters, but if it is pressurized for a 
long time when the motor is stopped, it may allow oil to enter through the lip.

enters, but if it is pressurized for a 
long time when the motor is stopped, it may allow oil to enter through the lip. When lubrication with an oil bath is 
conducted for gear engagement, for example, the oil level must be below the lip of the oil seal of the shaft, and the oil 
level must be adjusted so that the oil does nothing but splash on the lip.
```

---

## 第 259 頁
**本頁字數:** 872 字

### 內容摘要:
```text
Use environment for servo motors 
245 
Diameters of the oil seal lips of motor shafts 
Model 
Oil seal inner 
diameter 
αiS 0.2-D, αiS 0.3-D 
φ10 [mm] 
αiS 0.5-D, αiS 1-D, αiS 1.5-D (including HV) 
φ14.9 [mm] 
αiS 2-D, αiS 4-D (including HV), αiF 1-D, αiF 2-D 
φ15 [mm] 
αiS 8-D, αiS 12-D, αiS 18-D, αiF 4-D, αiF 8-D (including HV) 
φ24 [mm] 
αiS 22-D, αiS 30-D, αiS 40-D, αiF 12-D, αiF 22-D (including HV) 
(Only the straight shaft type of the following) 
αiS 50-D, αiS 60-D, αiF 30-D, αiF 40-D (including HV) 
* 
Including those equipped with cooling fans. 
φ35 [mm] 
(Only the taper shaft type of the following) 
αiS 50-D, αiS 60-D, αiF 30-D, αiF 40-D (including HV) 
* 
Including those equipped with cooling fans. 
φ38 [mm]

If the shaft is directed upward so that it is constantly immersed in oil, the oil seal of the motor alone does not provide 
sufficient sealing.
```

---

## 第 259 頁
**本頁字數:** 817 字

### 內容摘要:
```text
d upward so that it is constantly immersed in oil, the oil seal of the motor alone does not provide 
sufficient sealing. If grease is used for lubrication, the properties of the oil seal are generally impaired. In these cases, 
a special design is required. For example, another oil seal is mounted on the machine side and a drain is provided so 
that any oil passing through that seal can is discharged outside.

In such an environment in which the lip of the oil seal switches between dry and wet states repeatedly, if the cutting 
fluid flies about after the lip has worn in a dry state, the cutting fluid may easily enter the inside of the motor. In this 
case, provide a cover, etc. so that no cutting fluid is applied to the oil seal of the motor. 
Ensure that no pressure is applied to the lip of the oil seal.
```

---

## 第 259 頁
**本頁字數:** 752 字

### 內容摘要:
```text
o cutting fluid is applied to the oil seal of the motor. 
Ensure that no pressure is applied to the lip of the oil seal. 
The cutting fluid does not provide lubrication for the oil seal lip, so that the fluid may easily enter the seal. Also, water-
insoluble cutting fluid having high alkalinity may chemically react with the rubber material of oil seal, causing 
expansion and deterioration of lip part and easily entering. Provide a cover so that no cutting fluid is applied to the oil 
seal. 
The oil seal lip is made of rubber, and if foreign matters such as cutting chips get in, it will be easily worn, losing its 
sealing properties. Provide a cover, etc. to prevent cutting chips from entering near the lip.

g chips from entering near the lip.
```

---

## 第 260 頁
**本頁字數:** 694 字

### 內容摘要:
```text
Use environment for servo motors

246 
Motor coupling 
If a coupling box exists between the motor and the machine, employ the structure described below so that no cutting 
fluid builds up in the box.

Provide a cover for the top and sides of the coupling box.

Provide a drain hole at the bottom of the coupling box. The hole must be large enough to avoid clogging. Make sure 
that the motor is not exposed to any cutting fluid that splashes back from the drain hole.

<Fault example> 
The cutting fluid leaks from a gap in the accordion curtain to the motor area, and builds up in the coupling box. While 
the motor is moving, the cutting fluid ripples, splashing on the oil seal of the motor.
```

---

## 第 260 頁
**本頁字數:** 629 字

### 內容摘要:
```text
s up in the coupling box. While 
the motor is moving, the cutting fluid ripples, splashing on the oil seal of the motor. The cutting fluid enters the inside 
of the motor there in large quantities, deteriorating the insulation of the motor.

Connectors 
Note the following points on use:

Make sure that no cutting fluid is introduced to the motor via cables. If the motor connector is used horizontally, this 
can be accomplished by forming a slack in the cable.

If the motor connector is directed upward, the cutting fluid collects into the cable connector. Whenever possible, direct 
the motor connector sideways or downward.
```

---

## 第 261 頁
**本頁字數:** 898 字

### 內容摘要:
```text
Use environment for servo motors 
247

Due to flapping of the cable, load is applied to the connector, and when the mating part is shaken repeatedly, it may 
lead to connection failure or degradation of waterproof performance. 
With reference to "II.1.3.5. Caution(P.192)", take appropriate measures such as fixing the cable to the machine so as 
not to apply load to the connector.

If there is a possibility of the power line and the power connector getting wet, it is recommended to use the water-
proof connector plug recommended in this manual for the connector and an oil-proof cable as the power line. 
(Oil-proof cable example: PUR (polyurethane) series made by LAPP)

If using a conduit hose for cable protection purposes, use the seal adapter recommended in this manual.

The feedback cable connector provides IP67 waterproof performance when it is engaged with the Pulsecoder 
connector.
```

---

## 第 261 頁
**本頁字數:** 641 字

### 內容摘要:
```text
l.

The feedback cable connector provides IP67 waterproof performance when it is engaged with the Pulsecoder 
connector. If the feedback cable connector is not fully engaged, the cutting fluid will enter the inside of the Pulsecoder 
from the connector, possibly causing a failure. Install the connector properly in accordance with the feedback cable 
engagement procedure described in this manual and check that it is engaged securely. 
If the feedback cable connector cannot provide sufficient waterproof due to an assembly failure, the cutting fluid will 
enter the inside of the Pulsecoder from the connector, possibly causing a failure.
```

---

## 第 261 頁
**本頁字數:** 835 字

### 內容摘要:
```text
mbly failure, the cutting fluid will 
enter the inside of the Pulsecoder from the connector, possibly causing a failure. When assembling a feedback cable 
connector, assemble it properly in accordance with the operator's manual issued by the connector manufacturer.

Notes on cutting fluid 
Cutting fluid containing highly active sulfur or chlorine, oil-free cutting fluid called synthetic cutting fluid, or highly 
alkaline, water-soluble cutting fluid in particular significantly affect the CNC, motor or amplifier. Even when these 
components are protected from direct spraying of cutting fluid, problems as described below may arise. So special 
care should be taken.

- Cutting fluid containing highly active sulfur or chlorine 
Some cutting fluids containing sulfur or chlorine show extremely high activity of sulfur or chlorine.
```

---

## 第 261 頁
**本頁字數:** 608 字

### 內容摘要:
```text
ulfur or chlorine 
Some cutting fluids containing sulfur or chlorine show extremely high activity of sulfur or chlorine. Ingress of such 
cutting fluid into the CNC, motor, or amplifier can cause corrosion of copper, silver, and so on used as parts' 
materials, therefore resulting in parts' failures.

- Synthetic cutting fluid with high permeability 
Some synthetic type cutting fluids that use polyalkylene glycol (PAG) as a lubricant have extremely high permeability. 
Such cutting fluid can easily penetrate into the motor or device through packing and so on even if the motor or device 
is sealed well.
```

---

## 第 261 頁
**本頁字數:** 649 字

### 內容摘要:
```text
uid can easily penetrate into the motor or device through packing and so on even if the motor or device 
is sealed well. Penetration of such cutting fluid into the CNC, motor, or amplifier can deteriorate insulation or cause 
parts' failures.

- Highly alkaline, water-soluble cutting fluid 
Some cutting fluids that strengthen pH by alkanolamine show strong alkalinity of pH10 or higher when diluted to the 
standard level. Attachment of such cutting fluid to the CNC, motor, or amplifier, or penetration of such cutting fluid into 
them can cause chemical reaction with plastic and so on, therefore resulting in corrosion or deterioration of them.
```

---

## 第 262 頁
**本頁字數:** 872 字

### 內容摘要:
```text
Use environment for servo motors

NOTE 
Refer to "I.3.2. Outline drawings(P.117)" for wiring orifice diameter.

Cooling fan 
The protection class of cooling fan is not IP67. In an environment exposed to a cutting fluid, do not employ a motor 
with a cooling fan. 
If lubricant or cutting fluid mist, particles, or cutting chips are drawn into the cooling fan, the air holes in the cooling fan 
and the blades of the fan motor will clog, causing the cooling capacity to reduce. Employ a machine structure that 
allows clean, cooling air to be fed into the motor.

To ensure a sufficient volume of cooling air, provide sufficient space behind the cooling fan as follows: (Same applies 
to rear exhaust) 
 
αiS 50 FAN-D, αiS 60 FAN-D, αiF 40 FAN-D (including HV): 80mm or above

es 
to rear exhaust) 
 
αiS 50 FAN-D, αiS 60 FAN-D, αiF 40 FAN-D (including HV): 80mm or above
```

---

## 第 265 頁
**本頁字數:** 425 字

### 內容摘要:
```text
Data for selecting the αiPS 
251 
A. 
Data for selecting the αiPS 
1. For details about the selection method of the αiPS, refer to "Selecting the αiPS-D" of "SERVO AMPLIFIER αi-D 
series DESCRIPTIONS" (B-65552EN). 
2. The output values shown herein are intended for selection purposes only and do not guarantee the output of the 
servo motor. 
3. The continuous rated output and maximum output at acceleration may be changed.
```

---

## 第 268 頁
**本頁字數:** 785 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine tool 
B-
65542EN/01 
254 
B. 
Notes on using the servo motor for live tool applications of a 
machine tool 
This appendix contains the output graphs and torque graphs applicable when the FANUC SERVO MOTOR αi-D series is 
used for live tool applications of a machine tool, as well as the notes on such use of the servo motor. 
The output graphs and torque graphs of 4 representative models with a maximum rotation speed of 6000 [min-1] and 16 
representative models with a maximum rotation speed of 8000 [min-1] are shown here. 
B.1. 
Output graphs and torque graphs 
This section shows the output graphs and torque graphs of servo motors (models with a maximum rotation speed of 6000 
[min-1] and 8000[min-1]). 
1.
```

---

## 第 268 頁
**本頁字數:** 640 字

### 內容摘要:
```text
ut graphs and torque graphs of servo motors (models with a maximum rotation speed of 6000 
[min-1] and 8000[min-1]). 
1. The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque. 
2. The presented output values are those of the motor shaft output, not the data for selecting the αiPS.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 269 頁
**本頁字數:** 515 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine 
tool 
255 
αiS 0.3/8000-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 270 頁
**本頁字數:** 543 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine tool 
B-
65542EN/01 
256 
αiS 1/8000-D, αiS 1/8000HV-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 271 頁
**本頁字數:** 529 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine 
tool 
257 
αiS 2/6000-D, αiS 2/6000HV-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 272 頁
**本頁字數:** 543 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine tool 
B-
65542EN/01 
258 
αiS 4/6000-D, αiS 4/6000HV-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 273 頁
**本頁字數:** 529 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine 
tool 
259 
αiS 8/6000-D, αiS 8/6000HV-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 274 頁
**本頁字數:** 545 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine tool 
B-
65542EN/01 
260 
αiS 12/6000-D, αiS 12/6000HV-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 275 頁
**本頁字數:** 322 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine 
tool 
261 
αiS 22/6000-D, αiS 22/6000HV-D

* 
The intermittent operating zone represents the instantaneous maximum output at acceleration (torque) of the 
servo motor. 
It does not indicate the 30-minute rated output/torque or S3 rated output/torque.
```

---

## 第 276 頁
**本頁字數:** 707 字

### 內容摘要:
```text
Notes on using the servo motor for live tool applications of a machine tool 
B-
65542EN/01 
262 
B.2. 
Notes on using the servo motor for live tool applications 
To protect the servo amplifier, ensure that the load inertia moment does not exceed the moment of inertia of rotor. 
When dynamic brake is applied exceeding the above range, the inside of the servo amplifier may be heated abnormally, 
leading to burning of the servo amplifier. Be sure to calculate the load moment of inertia correctly.  
If the servo amplifier is used exceeding the above range, please contact FANUC.  
For details of the allowable value of the load inertia moment and the dynamic brake, see "II.2. Motor selection(P.199)."

1.
```

---

## 第 276 頁
**本頁字數:** 855 字

### 內容摘要:
```text
details of the allowable value of the load inertia moment and the dynamic brake, see "II.2. Motor selection(P.199)."

1. Unlike for the FANAC spindle motor αi-D series, "short-time rated outputs" exceeding the continuous rated output, 
such as 30-minute (S2) rated output and S3 rated output, are not defined for the FANUC SERVO MOTOR αi-D 
series. TUV certification has not been obtained in relation to short-time rated outputs, and these outputs and 
operations based on such outputs are not guaranteed.  
2. Before using the live tool beyond the continuous rated output on the rotary tool axis, be sure to check whether the 
desired operation is possible using the actual machine. If you intend to cite short-time rated output S2 or S3 as a 
nominal characteristic of the machine (rotary tool axis), you must take full responsibility for doing so.  
3.
```

---

## 第 276 頁
**本頁字數:** 807 字

### 內容摘要:
```text
S3 as a 
nominal characteristic of the machine (rotary tool axis), you must take full responsibility for doing so.  
3. Continuous operation with torque exceeding the continuous operating zone may generate the overheat alarm or 
OVC alarm.  
4. Even at no load, the temperature may exceed 100°C during high-speed rotation. Use it with a surrounding 
environment where sufficient heat discharge effect can be obtained by attaching a motor to a flange with good 
heat discharge capability. Before using the servo motor, check that the heat from the servo motor does not 
adversely affect the machine.  
5. When selecting the αiPS, calculate the required αiPS capacity by using the values of the "Data for selecting the 
αiPS" of each servo motor.  
For "Data for selecting the αiPS", refer to the appendix "A.
```

---

## 第 276 頁
**本頁字數:** 783 字

### 內容摘要:
```text
f the "Data for selecting the 
αiPS" of each servo motor.  
For "Data for selecting the αiPS", refer to the appendix "A. Data for selecting the αiPS(P.251) " or "SERVO 
AMPLIFIER αi-D series DESCRIPTIONS" (B-65552EN).  
6. For details about the selection of the αiPS and selection method, refer to "SERVO AMPLIFIER αi-D series 
DESCRIPTIONS" (B-65552EN).  
7. If you have any concerns, please contact FANUC.  
B.3. 
CNC functions for using the servo motor for the spindle or live tool 
For details of axis control function using the servo motor, refer to the sections about "Spindle control function using servo 
motor" of “Series 30i/31i/32i/35i-MODEL B DESCRIPTIONS” (B-64482EN) and "Series 0i-MODEL F DESCRIPTIONS" (B-
64602EN).

and "Series 0i-MODEL F DESCRIPTIONS" (B-
64602EN).
```

---

