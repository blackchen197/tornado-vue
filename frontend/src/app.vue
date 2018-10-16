<html>
<head>
  <meta charset="utf-8">
  <title>view file</title>

  <link href="../static/assets/css/bootstrap.min.css" rel="stylesheet" />
  <link href="../static/assets/css/animate.min.css" rel="stylesheet"/>

  <link href="../static/assets/css/paper-dashboard.css" rel="stylesheet"/>

  <link href="../static/assets/css/demo.css" rel="stylesheet" />

  <link href="../static/assets/css/themify-icons.css" rel="stylesheet">
  <script src="../static/js/jquery-3.3.1.min.js"></script>


   <link href="../static/assets/css/themify-icons.css" rel="stylesheet">
   <script src="../static/js/jquery-3.3.1.min.js"></script>    

  <style type="text/css">
      .tjcx li{
            list-style: none;
            color: #9d9d9d;
      }
      .tjcx li input{
            border-radius:5px;
            padding: 7px 0px;
            margin: 5px 0px;
	    width: 15%;
      }
      .tjcx2 li{
            list-style: none;
            margin-left: 5px;

      }

      .tjcx2 select {
            border-radius:5px;
            padding: 6px 13px;
            margin: 0px 3px;
      }
      .tjcx2 input{
            border-radius:5px;
            padding: 4px 5px;
            margin: 0px 3px;
      }
      .p2{
            padding-left: 3px;
        }
      .p2 a{
            color: black;
            margin-right:83px;
      }
      .header p{
            margin-left: 44px;
            font-size: 15px;
            font-weight: 600;
      }

      .a1{
            font-weight:500;color: white;background-color: deepskyblue;border-radius:9px;padding: 5px 20px;
        }
      .a1:hover{
            background-color: green;
            color: white;
      }

      .ssr a{
          color: deepskyblue;
          padding:5px 5px;
          font-size: 16px;

      }

    </style>

</head>
<body>
<div class="wrapper">
	<div class="sidebar" data-background-color="white" data-active-color="danger">


    	<div class="sidebar-wrapper">
            <div class="logo">
                <a href="#" class="simple-text">
                   N_page
                </a>
            </div>

            <ul class="nav">
                <li  class="active">
                    <a href="/">
                        <i class="ti-map"></i>
                        <p>N_page</p>
                    </a>
                </li>
            </ul>
    	</div>
    </div>

    <div class="main-panel">
		<nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar bar1"></span>
                        <span class="icon-bar bar2"></span>
                        <span class="icon-bar bar3"></span>
                    </button>
                    <a class="navbar-brand" href="#">search</a>
                </div>

            </div>
        </nav>


        <div class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12" style="background-color: white">
                        <div style="width:100%;">
                            <form action="/uploads" enctype='multipart/form-data' method='POST'>
                                <input type="file" name="file"  style="margin-top:20px;"/>
                                <p style="color: red">chiose</p>
                                <input type="file" name="xml"  style="margin-top:20px;"/>
                                <p style="color: red">xy</p>
                                <input type="submit" value="upload" class="button-new" style="margin-top:15px;"/>
                                <br>
                                <br>
                                <input type="button" onclick="buy()" value="image" style="background-color: red;color: white" />
                            </form>
                            <div style="float:left; width:50%;" id="g">
                                <img src=".{{ image }}" id="kp" class="im" width="600" >
                            </div>
                            <div style="float:right; width:50%;">
                                <table class="table table-striped" id="tb1" style="width: 450px">
                                    <thead style="background-color: skyblue">
                                        <th>con</th>
                                    </thead>
                                    <tbody id ="tb1">
                                        {% for foo in dic %}
                                            <tr>
                                            <td>{{ foo }}</td>

                                            </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer class="footer">
            <div class="container-fluid">
                <nav class="pull-left">
                    <ul>

                        <li>
                            <a href="#">
                                N_page
                            </a>
                        </li>
                        <li>
                            <a href="">
                               Contact
                            </a>
                        </li>
                        <li>
                            <a href="#/license">
                                lic
                            </a>
                        </li>
                    </ul>
                </nav>
                <div class="copyright pull-right">
                    &copy; <script>document.write(new Date().getFullYear())</script><a href="#"></a><a href="" target="_blank" title=""></a><a href="" title="" target="_blank"></a>
                </div>
            </div>
        </footer>
    </div>
</div>



<script src="../static/layer/layer.js"></script>
<script type="text/javascript">
    function buy() {
        document.getElementById('g').innerHTML = '<img src="{{ image }}" id = "kp" class="im" width="600" >'
    }
    function bub() {
        //a = $("#kp").attr("src");
        //if(a === '../static/hcp/{{ image }}'){
           // alert('chiose...')
        //}else{
        document.getElementById('g').innerHTML = '<img src="../static/hcp/{{ fliepath }}" id = "kp" class="im" width="600" >'

    }

    function ck(values) {
        layer.open({
                type: 2,
                title: 'Details',
                maxmin: true,
                area: ['1700', '800'],
                content: '/invoice?ids='+values,
        });
    }

     function ck2(values) {
        var r = confirm("ok");
        if(r == true){
            $.ajax({
                type: 'GET',
                url: '/invoice3?ids='+values,
                dataType: 'json',
                success: function (smg) {
                    $("#pps").load(location.href + " #pps");
                },
                error: function (msg) {
                    alert(msg.type)
                }
            });
        }
    }
</script>
</body>
</html>