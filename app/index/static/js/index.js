$('summary').on('click', e =>{
    let icon = $(e.target).find('i.chevron');
    $(icon).toggleClass('fa-chevron-right fa-angle-down')
});

$('summary .chevron').on('click', e =>{
    $(e.target).toggleClass('fa-chevron-right fa-angle-down')
});

function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML = Math.floor(progress * (end - start) + start);
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

let scrolls = 0;

$(window).scroll(function(){
  function elementScrolled(elem)
  {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();
    var elemTop = $(elem).offset().top;
    return ((elemTop <= docViewBottom) && (elemTop >= docViewTop));
  }


  if(elementScrolled('.stats')) {

    if(scrolls <= 0){
      console.log(scrolls);
      const projectElement = document.getElementById("projectsTotal");
      animateValue(projectElement, 0, 5000, 5000);

      const partnersElement = document.getElementById("yearsTotal");
      animateValue(partnersElement, 0, 5, 5000);

      const employeesElement = document.getElementById("clientsTotal");
      animateValue(employeesElement, 0, 649, 5000);
      const followersTotal = document.getElementById("followersTotal");
      animateValue(followersTotal, 0, 2200, 5000);
      scrolls ++;
    }
  }
});