
        var li_input = $('.li-input')[0];
        var li_textarea = $(".li-textarea")[0];
        var li_select = $(".li-select")[0];
        var ol_form = document.querySelector("#ol-form");

        if (li_input) {
            li_input.style.display = 'none';
            li_textarea.style.display = 'none';
            li_select.style.display = 'none';
        };

        let count_input = 0;
        let count_textarea = 0;
        let count_select = 0;

        $(document).on('click', '.del-form', function() {
            var for_del = this.parentElement.parentElement;
            for_del.remove()
        });

        $(document).on('click', '.del-select-name', function() {
             var select = this.previousElementSibling;
             var new_options = select.options[select.selectedIndex];
             new_options.remove();
        });
        $(document).on('click', '.add-select-name', function() {
             let select_name = this.previousElementSibling.value;
             var select = this.nextElementSibling.nextElementSibling.nextElementSibling;
             var new_options = this.nextElementSibling.nextElementSibling.nextElementSibling.options;
             new_options[new_options.length]= new Option(select_name,select_name,true);
             $(select).val(select_name);
             this.previousElementSibling.value = '';
        });

        $(document).on('click', '#submit-form', function(e) {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            var all_li = this.form.children[1].children;
            var data_form = document.getElementById('id_name').value;

            var input_forms_all = {};
            var textarea_forms_all = {};
            var select_forms_all = {};

            var input_count = 1
            var textarea_count = 1
            var select_count = 1

            for (let elem of all_li) {
                if (elem.className) {
                    if (elem.className == "li-input") {
                        if (elem.children[2].children[0].children[0].value) {
                            name = elem.children[2].children[0].children[0].value;
                            description = elem.children[2].children[1].children[0].value;
                            if (name != '' || description!= '') {
                                input_forms_all[input_count] = {}
                                input_forms_all[input_count]['name'] = name;
                                input_forms_all[input_count]['description'] = description;
                                input_count ++;
                            }
                        }
                    };

                    if (elem.className == "li-textarea") {
                        if (elem.children[2].children[0].children[0].value) {
                            name = elem.children[2].children[0].children[0].value;
                            description = elem.children[2].children[1].children[0].value;

                            if (name != '' || description!= '') {
                                textarea_forms_all[textarea_count] = {}
                                textarea_forms_all[textarea_count]['name'] = name;
                                textarea_forms_all[textarea_count]['description'] = description;
                                textarea_count ++;
                            }
                        }
                    };
                    if (elem.className == "li-select") {
                        var name = elem.children[1].children[0].value;
                        var description = elem.children[2].children[0].value;
                        select = elem.children[7];
                        select_options = [];
                        var options = select.getElementsByTagName('option');
                        for (var i=0; i<options.length; i++)  {
                            if (options[i].value) {
                                select_options.push(options[i].value);
                            }
                        }
                        if (name != '' || description!= '' || select_options.length > 0) {
                            select_forms_all[select_count] = {}
                            select_forms_all[select_count]['name'] = name;
                            select_forms_all[select_count]['description'] = description;
                            select_forms_all[select_count]['choices'] = select_options;
                            select_count ++;
                        }
                    };
                }
            };

            input_forms_all = JSON.stringify(input_forms_all);
            textarea_forms_all = JSON.stringify(textarea_forms_all);
            select_forms_all = JSON.stringify(select_forms_all);

            e.preventDefault();
            $.ajax({
                  headers: {'X-CSRFToken': '{{ csrf_token }}'},
                  type: "POST",
                  url: "{% url 'data_form_create' %}",
                  url: "",

                  data: {
                      'csrfmiddlewaretoken': csrftoken,
                      'data_form': data_form,
                      input_forms_all: input_forms_all,
                      textarea_forms_all: textarea_forms_all,
                      select_forms_all: select_forms_all
                      },
                  dataType: 'json',
                    error : function(data) {
                        if ( data.status == 200) {
                           window.location.href = "../";
                        };
                    }

              });
        });

        $(document).on('click', '#submit-form-update', function(e) {

            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            var all_li = this.form.children[1].children;
            var data_form = document.getElementById('id_name').value;
            var input_forms_all_new = {};
            var textarea_forms_all_new = {};
            var select_forms_all_new = {};

            var input_forms_all_edit = {};
            var textarea_forms_all_edit = {};
            var select_forms_all_edit = {};

            var input_count = 1
            var textarea_count = 1
            var select_count = 1

            for (let elem of all_li) {
                if (elem.className) {
//                    Создание

                    if (elem.className == "li-input") {
                        if (elem.children[2].children[0].children[0].value) {
                            name = elem.children[2].children[0].children[0].value;
                            description = elem.children[2].children[1].children[0].value;
                            input_forms_all_new[input_count] = {}
                            input_forms_all_new[input_count]['name'] = name;
                            input_forms_all_new[input_count]['description'] = description;
                            input_count ++;
                        }
                    };
                    if (elem.className == "li-textarea") {
                        if (elem.children[2].children[0].children[0].value) {
                            name = elem.children[2].children[0].children[0].value;
                            description = elem.children[2].children[1].children[0].value;
                            textarea_forms_all_new[textarea_count] = {}
                            textarea_forms_all_new[textarea_count]['name'] = name;
                            textarea_forms_all_new[textarea_count]['description'] = description;
                            textarea_count ++;
                        }
                    };
                    if (elem.className == "li-select") {
                        var name = elem.children[1].children[0].value;
                        var description = elem.children[2].children[0].value;
                        select = elem.children[7];
                        select_options = [];
                        var options = select.getElementsByTagName('option');
                        for (var i=0; i<options.length; i++)  {
                            if (options[i].value) {
                                select_options.push(options[i].value);
                            }
                        }
                        if (name != '' || description!= '' || select_options.length > 0) {
                            select_forms_all_new[select_count] = {}
                            select_forms_all_new[select_count]['name'] = name;
                            select_forms_all_new[select_count]['description'] = description;
                            select_forms_all_new[select_count]['choices'] = select_options;
                            select_count ++;
                        }
                    };
//                    Редактирование

                    if (elem.className.includes("edit-li-input-form-")) {
                       var numId = parseInt(elem.className.match(/\d+/));
                       var value = elem.children[2].children[0].children[0].value;
                       var description = elem.children[2].children[1].children[0].value;

                       input_forms_all_edit[numId] = {}
                       input_forms_all_edit[numId]['value'] = value;
                       input_forms_all_edit[numId]['description'] = description;
                    };

                    if (elem.className.includes("edit-li-textarea-form-")) {
                        var numId = parseInt(elem.className.match(/\d+/));
                        var value = elem.children[2].children[0].children[0].value;
                        var description = elem.children[2].children[1].children[0].value;

                       textarea_forms_all_edit[numId] = {}
                       textarea_forms_all_edit[numId]['value'] = value;
                       textarea_forms_all_edit[numId]['description'] = description;
                    };

                    if (elem.className.includes("edit-li-select-form-")) {
                        var numId = parseInt(elem.className.match(/\d+/))
                        var description = elem.children[2].children[0].value;
                        var select_form_name = elem.children[1].children[0].value;
                        select = elem.children[7];
                        select_options = [];
                        var options = select.getElementsByTagName('option');
                            for (var i=0; i<options.length; i++)  {
                                if (options[i].value) {
                                    select_options.push(options[i].value);
                                }
                            }
                        select_forms_all_edit[numId] = {}
                        select_forms_all_edit[numId]['name'] = select_form_name;
                        select_forms_all_edit[numId]['description'] = description;
                        select_forms_all_edit[numId]['choices'] = select_options;
                    };
                }
            };

            input_forms_all_edit = JSON.stringify(input_forms_all_edit);
            textarea_forms_all_edit = JSON.stringify(textarea_forms_all_edit);
            select_forms_all_edit = JSON.stringify(select_forms_all_edit);
            input_forms_all_new = JSON.stringify(input_forms_all_new);
            textarea_forms_all_new = JSON.stringify(textarea_forms_all_new);
            select_forms_all_new = JSON.stringify(select_forms_all_new);


            e.preventDefault();
            $.ajax({
                  headers: {'X-CSRFToken': '{{ csrf_token }}'},
                  type: "POST",
                  url: "",
                  data: {
                      'csrfmiddlewaretoken': csrftoken,
                      'data_form': data_form,
                      input_forms_all_new: input_forms_all_new,
                      textarea_forms_all_new: textarea_forms_all_new,
                      select_forms_all_new: select_forms_all_new,
                      input_forms_all_edit: input_forms_all_edit,
                      'textarea_forms_all_edit': textarea_forms_all_edit,
                      'select_forms_all_edit': select_forms_all_edit,
                      },
                  dataType: 'json',
                    error : function(data) {
                        if ( data.status == 200) {
                           window.location.href = "../";
                        };
                    }

              });

        });

          $(function(){
              $("#add-input").click(function(){
                    let li_input2 = li_input.cloneNode(true);
                    li_input2.id += String(count_input + 1);
                    li_input2.style.display = '';

                    li_input2.children[2].children[0].children[0].id += String(count_select + 1);
                    let div = document.createElement('div');
                    div.className = "del";
                    div.innerHTML = "<button type ='button' class='del-form'>Удалить поле</button>";
                    li_input2.append(div);

                    count_input ++;
                    ol_form.appendChild(li_input2);
              });
              $("#add-textarea").click(function(){
                    let li_textarea2 = li_textarea.cloneNode(true);
                    li_textarea2.id += String(count_select + 1);
                    li_textarea2.style.display = '';

                    let div = document.createElement('div');
                    div.className = "del";
                    div.innerHTML = "<button type ='button' class='del-form'>Удалить поле</button>";
                    li_textarea2.append(div);
                    count_textarea ++;
                    ol_form.appendChild(li_textarea2);
              });
              $("#add-select").click(function(){
                    let li_select2 = li_select.cloneNode(true);
                    li_select2.id += String(count_select + 1);
                    li_select2.style.display = '';

                    li_select2.children[0].value = '';

                    let div = document.createElement('div');
                    div.className = "del";
                    div.innerHTML = "<button type ='button' class='del-form'>Удалить поле</button>";
                    li_select2.append(div);
                    count_select ++;
                    ol_form.appendChild(li_select2);
              });
          });