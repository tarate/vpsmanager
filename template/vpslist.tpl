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

a {
	text-decoration:none;
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
   min-width:1000px;
   padding:5px;
   width:950px;
   }
.form-title {
   margin-bottom:0px;
   color: #725129;
   text-shadow: #fdf2e4 0 1px 0;
   }
.form-field {
   border: 1px solid #c9b7a2;
   -webkit-border-radius: 4px;
   -moz-border-radius: 4px;
   border-radius: 4px;
   }
table {
   border-collapse: collapse;
   border: 1px solid #999;
   }
.submit-container {
   width:20px;
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
		<div class="form-container">
			<h3 class="form-title">Tarate VPS List</h1>
			<div align="right" style="margin-right:95px">
				<span class="submit-button" align="right"><a href="/vps/add">ADD New</a></span>
				<br />
				<br />
			</div>
			<table cellpadding="0" cellspacing="0" border="1px">
				<tr>
				<th width="50" class="form-title">ID</th>
				<th width="80" class="form-title">Vender</th>
				<th width="90" class="form-title">IP</th>
				<th width="150" class="form-title">Remark</th>
				<th width="80" class="form-title">Type</th>
				<th width="80" class="form-title">Price</th>
				<th width="80" class="form-title">Statue</th>
				<th width="80" class="form-title">Score</th>
				<th width="150" class="form-title">Last Update</th>
				</tr>
				%if result_data:
				%for record in result_data:
				%id, vender, ip, remark, status, type, score, updated_time, price = record
				<tr align="center">
				<td width="50" height="40" class="form-title">{{!id}}</td>
				<td width="80" height="40" class="form-title">{{vender.title()}}</td>
				<td width="90" height="40" class="form-title">{{ip}}</td>
				<td width="100" height="40" class="form-title">{{remark}}</td>
				<td width="80" height="40" class="form-title">{{type.title()}}</td>
				<td width="80" height="40" class="form-title">{{price}}</td>
				<td width="80" height="40" class="form-title">{{!status.title()}}</td>
				<td width="80" height="40" class="form-title">{{!score}}</td>
				<td width="170" height="40" class="form-title">{{updated_time}}</td>
			  </tr>
			  %end
			  %else:
			  <tr>
			  	<td colspan="9" align="center"> No Data Yet! </td>
			  </tr>
			  %end

		  </table>
		  <br />
		  <br />
		</div>
	</div>
</body>
</html>
