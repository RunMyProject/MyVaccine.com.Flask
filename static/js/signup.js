$(function() {
    $('#btnSignUp').click(function() { 
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                window.location.href = "/showMyVaccineSpace"
            },
            error: function(error) {
                $('#respSignUp').html(response)
                console.log(error)
            }
        })
    })
})