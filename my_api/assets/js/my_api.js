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

function hideLoginFormShowTestArea() {
    $('.login-form').hide('fast', function() {
        $('.api-test-area').show('fast');
    });
}

$(function() {
    var $username = $('#username');
    var $password = $('#password');
    var access_token = null;
    var refresh_token = null;

    $('#list-items').click(function() {
        addLogEntry('Requesting /items...');

        $.ajax({
            url: '/api/items',
            headers: {
                'Authorization': 'Bearer ' + access_token
            }
        })
        .done(function(data) {
            addLogEntry('Got response from /api/items request: ' + JSON.stringify(data));
        })
        .fail(function(data) {
            addLogEntry('Fail response from /api/items request: ' + JSON.stringify(data));
        });
    });

    $('#list-concepts').click(function() {
        addLogEntry('Requesting /api/concepts...');

        $.ajax({
            url: '/api/concepts',
            headers: {
                'Authorization': 'Bearer ' + access_token
            }
        })
        .done(function(data) {
            addLogEntry('Got response from /api/concepts request: ' + JSON.stringify(data));
        })
        .fail(function(data) {
            addLogEntry('Fail response from /api/concepts request: ' + JSON.stringify(data));
        });
    });

    $('#fss-login-button').click(function() {
        addLogEntry('Requesting access token from FSS...');

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
                url: fssRegisterByAccessTokenUrl,
                data: {
                    access_token: data.access_token
                }
            })
            .done(function(data) {
                addLogEntry('Got access token from FSS: ' + JSON.stringify(data));
                access_token = data.access_token;
                refresh_token = data.refresh_token;
                hideLoginFormShowTestArea();
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
    });

    $('#fsswp-login-button').click(function() {
        addLogEntry('Requesting access token from FSS...');

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
            addLogEntry('Exchanging FSS access token with My API access token (using parameters)... ');

            $.ajax({
                url: fsswpRegisterByAccessTokenUrl,
                data: {
                    'access_token': data.access_token,
                    'username': $username.val()
                }
            })
            .done(function(data) {
                addLogEntry('Got access token from FSS: ' + JSON.stringify(data));
                access_token = data.access_token;
                refresh_token = data.refresh_token;
                hideLoginFormShowTestArea();
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
    });
});