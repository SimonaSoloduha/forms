
        var ol_form = document.querySelector("#ol-form");

        $(document).on('click', '#submit-form-save', function(e) {
            const csrftoken = document.cookie.split('=')[1].split(';')[0];
            var all_elem = this.form.children;
            var input_forms_all = new Map();
            var textarea_forms_all = new Map();
            var select_forms_all = new Map();

            for (let elem of all_elem) {
                if (elem.className) {
                    if (elem.className.includes("input-")) {
                        var numId = parseInt(elem.className.match(/\d+/));
                        var value = elem.children[1].value;
                        input_forms_all.set(numId, value);
                    };
                    if (elem.className.includes("textarea-")) {
                        var numId = parseInt(elem.className.match(/\d+/));
                        var value = elem.children[1].value;
                        textarea_forms_all.set(numId, value);
                    };
                    if (elem.className.includes("select-")) {
                        var numId = parseInt(elem.className.match(/\d+/));
                        var value = elem.children[1].value;
                        select_forms_all.set(numId, value);
                    };
                }
            };

            input_forms_all = Object.fromEntries(input_forms_all);
            textarea_forms_all = Object.fromEntries(textarea_forms_all);
            select_forms_all = Object.fromEntries(select_forms_all);

            e.preventDefault();
            $.ajax({
                  headers: {'X-CSRFToken': '{{ csrf_token }}'},
                  type: "POST",
//                  url: "{% url 'site_form_list' %}",
//                  url: "/. site",
                  data: {
                      'csrfmiddlewaretoken': csrftoken,
                      'input_forms_all': input_forms_all,
                      'textarea_forms_all': textarea_forms_all,
                      'select_forms_all': select_forms_all,
                      },
                  dataType: 'json',
                  error : function(data) {
                        if ( data.status == 200) {
                           window.location.href = "../";
                        };
                    }

              });

        });
