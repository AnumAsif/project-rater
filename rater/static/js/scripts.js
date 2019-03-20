$(document).ready(function(){
  $(".radio").click(function(){
    var $design = $("input[name='d-rating']:checked").val();
    var $usability = $("input[name='u-rating']:checked").val();
    var $content = $("input[name='c-rating']:checked").val();

    $.ajax({
      'url':`/ajax/project/${$design}/`,
      'type':'POST',
      'data':$design,
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })
  })

    
  })