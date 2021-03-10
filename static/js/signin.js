$(function() {
    $('#btnSignIn').click(function() { 
        $.ajax({
            url: '/signIn',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $('#respSignIn').html(response)
                console.log(response)
            },
            error: function(error) {
                $('#respSignIn').html(response)
                console.log(error)
            }
        })
    })
})