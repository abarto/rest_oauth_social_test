var access_token = null;
var refresh_token = null;

Handlebars.registerHelper('list', function(items, options) {
    var out = "";

    for (item of items) {
        out = out + options.fn(item);
    }

    return out;
});

var itemListTemplate = Handlebars.compile($("#item-list-template").html());
var conceptListTemplate = Handlebars.compile($("#concept-list-template").html());

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

function save_tokens(data) {
    access_token = data.access_token;
    refresh_token = data.refresh_token;
}

$(function() {
    var $apiResponsePanel = $('#api-response-panel');
    var $username = $('#username');
    var $password = $('#password');

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

            var html = itemListTemplate({'items': data});

            $apiResponsePanel.html(html);
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

            var html = conceptListTemplate({'concepts': data});

            $apiResponsePanel.html(html);
        })
        .fail(function(data) {
            addLogEntry('Fail response from /api/concepts request: ' + JSON.stringify(data));
        });
    });

    $('#login-button').click(function() {
        addLogEntry('Requesting access token from My API...');

        $.ajax({
            url: 'http://localhost:8000/o/token/',
            method: 'POST',
            data: {
                username: $username.val(),
                password: $password.val(),
                grant_type: 'password',
                client_id: '4GyPYtpHrFVCykWHDkS8louGrV3QERWeH39PCR5h'
            }
        })
        .done(function(data) {
            addLogEntry('Got access token from My API: ' + JSON.stringify(data));
            save_tokens(data);
            hideLoginFormShowTestArea();
        })
        .fail(function(data, textStatus) {
            addLogEntry('Fail response requesting access token from My API: ' + JSON.stringify(data));
            showLoginErrors('Unable to log into <strong>My API</strong>. Check logs.')
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
                client_id: 'ZQcMr611iZMcUskTGoRcyZuhqCjZYy08lyOsWM5d'
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
                save_tokens(data);
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
                client_id: 'ZQcMr611iZMcUskTGoRcyZuhqCjZYy08lyOsWM5d'
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
                save_tokens(data);
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
