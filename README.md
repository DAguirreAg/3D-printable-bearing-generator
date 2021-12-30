# 3D-printable-bearing-generator
Generate 3D printable bearings according to your dimension constrains.

<p align="middle">
  <img src="/images/Turning test.gif" alt="Turning test of a 3D printed bearing" width=300>
</p>

## 1. Introduction
Many hobbyist face the problem of needing some bearings that are lightweight and cheap enough for their applications. However, more times than not, the available sizes don´t match your application or they are to much of an overkill to be used. To solve these issues I decided to develop a Fusion 360 script which generates bearings depending on your input parameters.

<p align="middle">
  <img src="/images/3D printed bearing.jpg" alt="Photo of a 3D printed bearing" width=200>

  <img src="/images/Generated Fusion 360 file.png" alt="Generated bearing" width=200>

  <img src="/images/Generated Fusion 360 file section.png" alt="A section view of the generated bearing" width=200>
</p>


## 2. How to use
Start by downloading and installing the script into your Fusion 360. Check [here](https://knowledge.autodesk.com/support/fusion-360/troubleshooting/caas/sfdcarticles/sfdcarticles/How-to-install-an-ADD-IN-and-Script-in-Fusion-360.html) for a quick guide.
 
Once installed open the script and modify the following bearing's parameters: 

<p align="middle">
  <img src="/images/Bearing parameters.png" alt="The input parameters to generate the bearing" width=500>
</p>

## 3. Assembly

For the assembly of the bearings follow next steps:
1. 3D print bearing's two parts.
2. Remove the support material
3. Place a BB ball into the outer part's groove and turn the outer part looking for positions in which the ball gets stuck. Clean those positions until the ball is able to rotate freely.
4. Repeat previous step in the inner part's groove, by placing a BB on it and turning the inner part. Make sure that the BB ball slides smoothly.

<p align="middle">
  <img src="/images/Check roughness outer part.jpg" alt="Check outer part´s roughness" width=300>

  <img src="/images/Check roughness inner part.jpg" alt="Check inner part´s roughness" width=300>
</p>

 
5. Place the inner part inside the outer part and align the holes.

<p align="middle">
  <img src="/images/Bearing parts alignment.jpg" alt="Alignment of the bearing parts" width=300>
</p>

6. Start inserting BBs until there is no more room left. During the process make sure to turn the bearing to detect any kind of blockage. If you encounter a blockage disassemble and check the surfaces again.


<p align="middle">
  <img src="/images/Inserting BB balls.jpg" alt="Insert BB balls into the bearing" width=300>
</p>

7. Finish by inserting BBs until there is no more room left.
8. Turn the bearing and see if it turns smoothly.


## 4. Disassembly
The disassembly process could be a little bit troublesome depending on the tolerances you used.

1. Align the insertion holes.
2. With a thin tool align on BB ball in a way it is below the insertion hole.
3. With another thin tool push the BB ball from behind though the extraction hole.
4. Repeat 2-3 steps until there are no BB balls left.
<p align="middle">
  <img src="/images/Disassemble process.jpg" alt="Disassemble process" width=300>
</p>

## 5. Software
The script works in the following manner:

1. Check the input parameters are correct
2. Draw the inner and outer circles and extrude them (create new body operation).
3. Draw the gap circle and extrude it (cut operation).
4. Draw the BB ball circle and revolute it (cut operation).
5. Draw the insertion and extraction circles and extrude them (cut operation).

## 6. Requirements
You should install/have the following:

* Fusion 360
* BB balls
* 3D printer


## Future functionalities

In future versions I would like to add a GUI interface for inputting the parameter values. I would also like to include other bearing models with optional features (assembly holes,...).

