function subtractYears(date, years) {
  date.setFullYear(date.getFullYear() - years);
  return date;
}

$(document).ready(function(){
  const now = new Date();
  const lastDatePossible = subtractYears(now, 60);
  const minDateOfBirth = subtractYears((new Date()), 18);
  console.log(lastDatePossible.getFullYear(), minDateOfBirth.getFullYear())
    $('.datepicker').datepicker({
      yearRange:[lastDatePossible.getFullYear(), minDateOfBirth.getFullYear()],
      format:'mm/dd/yyyy',
      setDefaultDate:true
    });
  M.updateTextFields();
  $('.sidenav').sidenav();


  M.updateTextFields();
  $('.sidenav').sidenav();
  });

