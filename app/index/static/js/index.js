$('summary').on('click', e =>{
    let icon = $(e.target).find('i.chevron');
    $(icon).toggleClass('fa-chevron-right fa-angle-down')
});

$('summary .chevron').on('click', e =>{
    $(e.target).toggleClass('fa-chevron-right fa-angle-down')
});