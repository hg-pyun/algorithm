var numUniqueEmails = function (emails) {
    var result = 0;

    var parsedEmails = [];

    emails.forEach(function (item) {

        var newString = '';

       // parse string
        var skip = false;
        for (var i = 0; i < item.length; i++) {
            var char = item[i];
            if (char === '@') break;
            if (char === '.' || skip) continue;
            if (char === '+') {
                skip = true;
                continue;
            }

            newString += char;
        }

        // add domain
        for (var j = i; j < item.length; j++) {
            newString += item[j];
        }

        if (newString !== '' && parsedEmails.indexOf(newString) === -1) {
            parsedEmails.push(newString);
            result++;
        }
    });

    return result;
};
