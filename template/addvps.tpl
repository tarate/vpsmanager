<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Add VPS</title>
<style type="text/css">
<!--
body {
	background-color: #F0F0F0;
}
.form-container {
   border: 1px solid #f2e3d2;
   background: #c9b7a2;
   background: -webkit-gradient(linear, left top, left bottom, from(#f2e3d2), to(#c9b7a2));
   background: -webkit-linear-gradient(top, #f2e3d2, #c9b7a2);
   background: -moz-linear-gradient(top, #f2e3d2, #c9b7a2);
   background: -ms-linear-gradient(top, #f2e3d2, #c9b7a2);
   background: -o-linear-gradient(top, #f2e3d2, #c9b7a2);
   background-image: -ms-linear-gradient(top, #f2e3d2 0%, #c9b7a2 100%);
   -webkit-border-radius: 8px;
   -moz-border-radius: 8px;
   border-radius: 8px;
   -webkit-box-shadow: rgba(000,000,000,0.9) 0 1px 2px, inset rgba(255,255,255,0.4) 0 0px 0;
   -moz-box-shadow: rgba(000,000,000,0.9) 0 1px 2px, inset rgba(255,255,255,0.4) 0 0px 0;
   box-shadow: rgba(000,000,000,0.9) 0 1px 2px, inset rgba(255,255,255,0.4) 0 0px 0;
   font-family: 'Helvetica Neue',Helvetica,sans-serif;
   text-decoration: none;
   vertical-align: middle;
   min-width:300px;
   padding:20px;
   width:400px;
   }
.form-field {
   border: 1px solid #c9b7a2;
   background: #e4d5c3;
   -webkit-border-radius: 4px;
   -moz-border-radius: 4px;
   border-radius: 4px;
   color: #c9b7a2;
   -webkit-box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(000,000,000,0.7) 0 0px 0px;
   -moz-box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(000,000,000,0.7) 0 0px 0px;
   box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(000,000,000,0.7) 0 0px 0px;
   padding:8px;
   margin-bottom:0px;
   width:280px;
   }
.form-field:focus {
   background: #fff;
   color: #725129;
   }
.form-container h2 {
   text-shadow: #fdf2e4 0 1px 0;
   font-size:18px;
   margin: 0 0 10px 0;
   font-weight:bold;
   text-align:center;
    }
.form-title {
   margin-bottom:0px;
   color: #725129;
   text-shadow: #fdf2e4 0 1px 0;
   }
.submit-container {
   margin:8px 0;
   text-align:right;
   }
.submit-button {
   border: 1px solid #447314;
   background: #6aa436;
   background: -webkit-gradient(linear, left top, left bottom, from(#8dc059), to(#6aa436));
   background: -webkit-linear-gradient(top, #8dc059, #6aa436);
   background: -moz-linear-gradient(top, #8dc059, #6aa436);
   background: -ms-linear-gradient(top, #8dc059, #6aa436);
   background: -o-linear-gradient(top, #8dc059, #6aa436);
   background-image: -ms-linear-gradient(top, #8dc059 0%, #6aa436 100%);
   -webkit-border-radius: 4px;
   -moz-border-radius: 4px;
   border-radius: 4px;
   -webkit-box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(255,255,255,0.4) 0 1px 0;
   -moz-box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(255,255,255,0.4) 0 1px 0;
   box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(255,255,255,0.4) 0 1px 0;
   text-shadow: #addc7e 0 1px 0;
   color: #31540c;
   font-family: helvetica, serif;
   padding: 8.5px 18px;
   font-size: 14px;
   text-decoration: none;
   vertical-align: middle;
   }
.submit-button:hover {
   border: 1px solid #447314;
   text-shadow: #31540c 0 1px 0;
   background: #6aa436;
   background: -webkit-gradient(linear, left top, left bottom, from(#8dc059), to(#6aa436));
   background: -webkit-linear-gradient(top, #8dc059, #6aa436);
   background: -moz-linear-gradient(top, #8dc059, #6aa436);
   background: -ms-linear-gradient(top, #8dc059, #6aa436);
   background: -o-linear-gradient(top, #8dc059, #6aa436);
   background-image: -ms-linear-gradient(top, #8dc059 0%, #6aa436 100%);
   color: #fff;
   }
.submit-button:active {
   text-shadow: #31540c 0 1px 0;
   border: 1px solid #447314;
   background: #8dc059;
   background: -webkit-gradient(linear, left top, left bottom, from(#6aa436), to(#6aa436));
   background: -webkit-linear-gradient(top, #6aa436, #8dc059);
   background: -moz-linear-gradient(top, #6aa436, #8dc059);
   background: -ms-linear-gradient(top, #6aa436, #8dc059);
   background: -o-linear-gradient(top, #6aa436, #8dc059);
   background-image: -ms-linear-gradient(top, #6aa436 0%, #8dc059 100%);
   color: #fff;
   }
-->
</style></head>
<body>
<div id="main" align="center">
	<form class="form-container" method="post" action="/vps/add">
		<table width="400" border="0">
		<th width="150" colspan="2" align="center" class="form-title"> Add New VPS </th>
  <tr>
    <td width="100" class="form-title">Vender</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_vender" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">AC</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_ac" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">OS</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_os" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">IP</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_ip" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">Root Pass</td>
    <td width="150" align="center" valign="middle"><input type="password" name="vps_root_passwd" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">CPanel Addr</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_cpanel_addr" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">CPanel User</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_cpanel_user" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">CPanel Pass</td>
    <td width="150" align="center" valign="middle"><input type="password" name="vps_cpanel_passwd" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">Remark</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_remark" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">Type</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_type" class="form-field" /></td>
  </tr>
  <tr>
    <td width="100" class="form-title">Price</td>
    <td width="150" align="center" valign="middle"><input type="text" name="vps_price" class="form-field" /></td>
  </tr>
  <tr>
  	<td colspan="2">
	&nbsp;
	</td>
  </tr>
  <tr>
    <td align="center" colspan="2">
	<input class="submit-button" type="submit" value="Submit" />
    &nbsp;&nbsp;&nbsp;&nbsp;
	<input class="submit-button" type="reset" value="Reset" />	</td>
  </tr>
</table>

	</form>
</div>
</body>
</html>
