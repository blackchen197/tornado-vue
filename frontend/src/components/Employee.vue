

<template>

<div class="col-md-6">
    <b-link :to="{ name: 'home'}">
        Назад
    </b-link>
    <b-link :to="{ name: 'salary', params: { id: this.employee.id }}" style="float:right">
        Список выплат
    </b-link>
    <b-form @submit="onSubmit" style="margin:10px">
        <b-form-group id="fioGroup" label="Фамилия И.О.:" label-for="fio">
            <b-form-input id="fio" type="text" v-model="employee.fio" required placeholder="Введите ФИО">
            </b-form-input>
        </b-form-group>
        <b-form-group id="phoneGroup" label="Телефон:" label-for="phone">
            <b-form-input id="phone" type="text" v-model="employee.phone" placeholder="Введите телефон">
            </b-form-input>
        </b-form-group>
        <b-form-group id="birthdayGroup" label="Дата рождения:" label-for="birthday">
            <date-picker v-model="employee.birthday" :config="options" id="birthday"></date-picker>
        </b-form-group>
        <b-form-group id="sexGroup" label="Пол:" label-for="sex">
            <b-form-radio-group id="sex" :options="sex" v-model="employee.sex">
            </b-form-radio-group>
        </b-form-group>
        <b-form-group id="departGroup" label="Отдел:" label-for="depart">
            <b-form-select id="depart" :options="depart" v-model="employee.depart">
            </b-form-select>
        </b-form-group>
        <b-button type="submit" size="sm" variant="primary" style="float:right">Сохранить</b-button>
        <b-button size="sm" variant="danger" @click="del()">Удалить</b-button>
    </b-form>
</div>

</template>

<script>

import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css';
import datePicker from 'vue-bootstrap-datetimepicker';
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';

export default {
    props: ['id'],
    title: `Сотрудник`,
    data() {
        return {
            date: new Date(),
            options: {
                format: 'DD-MM-YYYY',
                useCurrent: false,
                locale: 'ru',
            },
            sex: [
                'муж.', 'жен.'
            ],
            depart: [
                'Руководство', 'Бухгалтерия', 'IT'
            ],
            employee: Object(),
        }
    },
    components: {
        datePicker
    },
    methods: {
        onSubmit(evt) {
                evt.preventDefault();
                const path = 'http://localhost:5000/api/info/' + this.employee.id;
                if (this.employee.sex == "муж.") {
                    this.employee.sexy = "0";
                } else {
                    this.employee.sexy = "1";
                }
                var vm = this
                axios.put(path, {
                        fio: this.employee.fio,
                        birthday: this.employee.birthday,
                        phone: this.employee.phone,
                        sex: this.employee.sexy,
                        depart: this.employee.depart,
                    })
                    .then(function(response) {
                        vm.$notify({
                          group: 'foo',
                          text: 'Успешно сохранено',
                          type: 'success',
                        });
                    })
                    .catch(function(error) {
                        console.log('error');
                        console.log(error);
                    });
            },

            del() {
                const path = 'http://localhost:5000/api/info/' + this.employee.id;
                var vm = this
                axios.delete(path)
                    .then(function(response) {
                        vm.$router.push({
                            path: '/'
                        });
                        vm.$notify({
                          group: 'foo',
                          text: 'Успешно удалено',
                          type: 'success',
                        });
                    })
                    .catch(function(error) {
                        console.log('error');
                        console.log(error);
                    });

            },
            getEmployee(id) {
                const path = 'http://localhost:5000/api/info/' + id
                axios(path)
                    .then(response => {
                        var info = response.data[0];
                        this.employee = info;
                        this.employee.sexy = info.sex;
                        if (info.sex > 0) {
                            this.employee.sex = 'жен.';
                        } else {
                            this.employee.sex = 'муж.';
                        }
                        this.employee.id = info.id;
                        this.employee.fio = info.fio.fio;
                        this.employee.depart = info.depart;
                        document.title = `Сотрудник - ` + this.employee.fio;
                    })
                    .catch(error => {
                        console.log('error');
                        console.log(error)
                    })
            }
    },

    created() {
        this.getEmployee(this.id);
    },
    watch: {
        '$route' () {
            this.getEmployee(this.id);
        }
    }
}

</script>
