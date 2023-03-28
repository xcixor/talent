function subtractYears(date, years) {
  date.setFullYear(date.getFullYear() - years);
  return date;
}

$(document).ready(function(){
  const now = new Date();
  const minDateOfBirth = subtractYears(now, 18);
    $('.datepicker').datepicker({
      defaultDate: minDateOfBirth,
      setDefaultDate: true,
      maxDate:minDateOfBirth
    });
    M.updateTextFields();
  });

