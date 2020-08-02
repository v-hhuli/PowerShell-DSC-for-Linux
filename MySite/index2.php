<?php
         if(isset($_GET['off1'])){
				 $setmode4 = shell_exec("gpio -g mode 4 out");
                 $gpio_off = shell_exec("gpio -g write 4 1");
        }
         else if(isset($_GET['on1'])){
			     $setmode4 = shell_exec("gpio -g mode 4 out");
                 $gpio_on = shell_exec("gpio -g write 4 0");
        }
         if(isset($_GET['off2'])){
				 $setmode22 = shell_exec("gpio -g mode 22 out");
                 $gpio_off = shell_exec("gpio -g write 22 1");
        }
         else if(isset($_GET['on2'])){
				 $setmode22 = shell_exec("gpio -g mode 22 out");
                 $gpio_on = shell_exec("gpio -g write 22 0");
        }
         if(isset($_GET['off3'])){
				 $setmode6 = shell_exec("gpio -g mode 6 out");
                 $gpio_off = shell_exec("gpio -g write 6 1");
        }
         else if(isset($_GET['on3'])){
				 $setmode6 = shell_exec("gpio -g mode 6 out");
                 $gpio_on = shell_exec("gpio -g write 6 0");
        }
         if(isset($_GET['off4'])){
				 $setmode26 = shell_exec("gpio -g mode 26 out");
                 $gpio_off = shell_exec("gpio -g write 26 1"); 
        }
         else if(isset($_GET['on4'])){
				 $setmode26 = shell_exec("gpio -g mode 26 out");
                 $gpio_on = shell_exec("gpio -g write 26 0");
        }
		if(isset($_GET['off5'])){
				 $setmode13 = shell_exec("gpio -g mode 13 out");
                 $gpio_off = shell_exec("gpio -g write 13 1");
        }
         else if(isset($_GET['on5'])){
			     $setmode13 = shell_exec("gpio -g mode 13 out");
                 $gpio_on = shell_exec("gpio -g write 13 0");
        }
		if(isset($_GET['off6'])){
				 $setmode5 = shell_exec("gpio -g mode 5 out");
                 $gpio_off = shell_exec("gpio -g write 5 1");
        }
         else if(isset($_GET['on6'])){
			     $setmode5 = shell_exec("gpio -g mode 5 out");
                 $gpio_on = shell_exec("gpio -g write 5 0");
        }
		if(isset($_GET['off7'])){
				 $setmode20 = shell_exec("gpio -g mode 20 out");
                 $gpio_off = shell_exec("gpio -g write 20 1");
        }
         else if(isset($_GET['on7'])){
			     $setmode20 = shell_exec("gpio -g mode 20 out");
                 $gpio_on = shell_exec("gpio -g write 20 0");
        }
?>
<?php
		if(isset($_GET['off8'])){
                 $gpio_off = shell_exec("gpio -g write 17 0");		 
         }
         else if(isset($_GET['on8'])){
				 $setmode17 = shell_exec("gpio -g mode 17 out");
                 $gpio_on = shell_exec
				 ("gpio -g write 17 1
				 sleep 2
				 gpio -g write 17 0");
        }
?>
<?php
        
// Set up valid status list
$state4[0] = "<span style='background-color: #05ff05' >Open</span>";
$state4[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state22[0] = "<span style='background-color: #05ff05'>Open</span>";
$state22[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state6[0] = "<span style='background-color: #05ff05'>Open</span>";
$state6[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state26[0] = "<span style='background-color: #05ff05'>Open</span>";
$state26[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state17[0] = "<span style='background-color: #05ff05'>Open</span>";
$state17[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state13[0] = "<span style='background-color: #05ff05'>Open</span>";
$state13[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state5[0] = "<span style='background-color: #05ff05'>Open</span>";
$state5[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

$state20[0] = "<span style='background-color: #05ff05'>Open</span>";
$state20[1] = "<span style='background-color: #ff1b0a; color: #ffffff'>Closed</span>";

?>


<html>
<head>
 <meta name="viewport" content="width=device-width" />
 <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>
</head>
  <body bgcolor="#333333" style="color: #FFFFFF;">
  
  <h1 style="color: #4485b8;">My Observatory Web Server</h1>
<p>&nbsp;This page will control the power on my Observatory</p>
<h4>Control Panel</h4>
<iframe frameborder="0" height="255" width="500" scrolling="no" src="http://192.168.2.65:8888/"></iframe>
<br><br>
<form method="get" action="index2.php">
<table style="vertical-align: top; color: #000000;">
<thead>
<tr style="height: 23px; background-color: #8EBFE5;">
<td style="width: 140px; height: 23px; padding-left: 15px;">Device</td>
<td style="width: 100px; height: 23px; padding-left: 30px;">Turn On</td>
<td style="width: 100px; height: 23px; padding-left: 30px;">Turn Off</td>
<td style="width: 896px; height: 23px; padding-left: 10px;">State</td>
</tr>
</thead>
<tbody id="tableData">

<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px; "><strong>ASA Mount DDM60</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px; "><input type="submit" value="ON" name="on1"></td>
<td style="width: 100px; height: 25px; padding-left: 30px; "><input type="submit" value="OFF" name="off1"></td>
<td style="width: 896px; height: 25px; padding-left: 10px; "><?php $pinStatus4 = trim(shell_exec("gpio -g read 4"));
//returns 0 = low; 1 = high
echo $state4[$pinStatus4];?></td>

</tr>
<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>CCD Camera</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="ON" name="on2"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="OFF" name="off2"></td>
<td style="width: 896px; height: 25px; padding-left: 10px;"><?php $pinStatus22 = trim(shell_exec("gpio -g read 22"));
//returns 0 = low; 1 = high
echo $state22[$pinStatus22];?> </td>
</tr>
<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>MoonLight Focuser</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="ON" name="on3"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="OFF" name="off3"></td>
<td style="width: 896px; height: 25px; padding-left: 10px;"><?php $pinStatus6 = trim(shell_exec("gpio -g read 6"));
//returns 0 = low; 1 = high
echo $state6[$pinStatus6];?> </td>
</tr>
<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>Computer</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="ON" name="on4"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="OFF" name="off4"></td>
<td style="width: 896px; height: 25px; padding-left: 10px;"><?php $pinStatus26 = trim(shell_exec("gpio -g read 26"));
//returns 0 = low; 1 = high
echo $state26[$pinStatus26];?> </td>
</tr>

<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>Lights</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="ON" name="on5"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="OFF" name="off5"></td>
<td style="width: 896px; height: 25px; padding-left: 10px;"><?php $pinStatus13 = trim(shell_exec("gpio -g read 13"));
//returns 0 = low; 1 = high
echo $state13[$pinStatus13];?> </td>
</tr>

<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>Relay 6</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="ON" name="on6"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="OFF" name="off6"></td>
<td style="width: 896px; height: 25px; padding-left: 10px;"><?php $pinStatus5 = trim(shell_exec("gpio -g read 5"));
//returns 0 = low; 1 = high
echo $state5[$pinStatus5];?> </td>
</tr>

<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>Rack FAN</strong></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="ON" name="on7"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="OFF" name="off7"></td>
<td style="width: 896px; height: 25px; padding-left: 10px;"><?php $pinStatus20 = trim(shell_exec("gpio -g read 20"));
//returns 0 = low; 1 = high
echo $state20[$pinStatus20];?> </td>
</tr>


<tr style="height: 25px; background-color: #CECECE;" >
<td style="min-width: 140px; width: 160px; height: 25px; padding-left: 15px;"><strong>Roof Open/Close</strong></td>
<td style="width: 100px; height: 25px; padding-left: 5px;"><input type="submit" value="Roof Open/Close" name="on8"></td>
<td style="width: 100px; height: 25px; padding-left: 30px;"><input type="submit" value="Check Status" name="off8"></td>
<td style="width: 896px; height: 30px; padding-left: 0px;"><iframe style="width: 100%; height: 100%; border: none; margin: 0; padding: 0;" frameborder="0" scrolling="no" src="http://192.168.2.65/roof_status_sensor.php"></iframe></td>
</tr>


</table>

</form>
         
 </body>
</html>
