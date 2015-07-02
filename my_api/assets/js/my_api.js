function addLogEntry(text) {
    var date = new Date()

    var $logEntry = $('<div class="log-entry"><span class="log-timestamp">' + new Date().toUTCString() + '</span><span class="log-text">' + text + '<span></div>');

    var $logContent = $('.log-content');
    $logContent.append($logEntry);

    $logContent.scrollTop($logContent.prop('scrollHeight'));
}

function showLoginErrors(text) {
    $('.login-errors').html(text);
    $('.login-errors').show('fast').delay(2000).hide('fast');
}

$(function() {
    var $username = $('#username');
    var $password = $('#password');

    $('#fss-login-button').click(function() {
        addLogEntry('Requesting access token from FSS...');

        $('.login-form').hide('fast', function() {
            $('.api-test-area').show('fast');
        });

        /*
        $.ajax({
            url: 'http://localhost:8005/o/token/',
            method: 'POST',
            data: {
                username: $username.val(),
                password: $password.val(),
                grant_type: 'password',
                client_id: '7xgbGncy4u4QqNPuOhX6ge7drc5OKfzNkgN1uynS'
            }
        })
        .done(function(data) {
            addLogEntry('Got access token from FSS: ' + JSON.stringify(data));
            addLogEntry('Exchanging FSS access token with My API access token... ');

            $.ajax({
                url: fssRegisterByAccessTokenUrl + '?access_token=' + data.access_token
            })
            .done(function(data) {
                addLogEntry('Got access token from FSS: ' + JSON.stringify(data));
            })
            .fail(function(data, textStatus) {
                addLogEntry('Fail response exchanging access token from FSS: ' + JSON.stringify(data));
                showLoginErrors('Unable to log into <strong>My API</strong>. Check logs.')
            });
        })
        .fail(function(data, textStatus) {
            addLogEntry('Fail response requesting access token from FSS: ' + JSON.stringify(data));
            showLoginErrors('Unable to log into <strong>FSS</strong>. Check logs.')
        });
        */
    });
});