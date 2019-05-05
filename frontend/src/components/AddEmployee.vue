<template>
  <div class="col-md-6">
    <b-link :to="{ name: 'home'}">
      Назад
    </b-link>
    <b-form @submit="onSubmit"  style="margin:10px">
      <b-form-group id="fioGroup"
                    label="Фамилия И.О.:"
                    label-for="fio">
        <b-form-input id="fio"
                      type="text"
                      v-model="employe.fio"
                      required
                      placeholder="Введите ФИО">
        </b-form-input>
      </b-form-group>
      <b-form-group id="phoneGroup"
                    label="Телефон:"
                    label-for="phone">
        <b-form-input id="phone"
                      type="text"
                      v-model="employe.phone"
                      placeholder="Введите телефон">
        </b-form-input>
      </b-form-group>
      <b-form-group id="birthdayGroup"
                    label="Дата рождения:"
                    label-for="birthday">
      <date-picker v-model="employe.birthday" :config="options" id="birthday"></date-picker>
      </b-form-group>
      <b-form-group id="sexGroup"
                    label="Пол:"
                    label-for="sex">
        <b-form-radio-group id="sex"
                      :options="sex"
                      v-model="employe.sex">
        </b-form-radio-group>
      </b-form-group>
      <b-form-group id="departGroup"
                    label="Отдел:"
                    label-for="depart">
        <b-form-select id="depart"
                      :options="depart"
                      v-model="employe.depart">
        </b-form-select>
      </b-form-group>
      <b-button type="submit" size="sm" variant="primary" style="float:right">Сохранить</b-button>
    </b-form>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css';
import datePicker from 'vue-bootstrap-datetimepicker';
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';

  import axios from 'axios';
  export default {
    props: ['id'],
    title: `Сотрудник`,
    data() {
      return {
        options: {
          format: 'DD-MM-YYYY',
          useCurrent: false,
          locale:'ru',
        },
      sex: [
        'муж.', 'жен.'
      ],
      depart: [
        'Руководство', 'Бухгалтерия','IT'
      ],
        employe:Object()
      }
    },
    components: {
      datePicker
    },
    methods: {
      onSubmit (evt) {
      evt.preventDefault();
      const path = 'http://localhost:5000/api/info';
      if (this.employe.sex == "муж.") {this.employe.sexy = "0";} else{this.employe.sexy = "1";}
      var vm = this;
      axios.post(path,
        {
            fio: this.employe.fio,
            birthday: this.employe.birthday,
            phone: this.employe.phone,
            sex: this.employe.sexy,
            depart: this.employe.depart,
        }
      )
        .then(function (response) {
          vm.$router.push({path: '/' });
          vm.$notify({
            group: 'foo',
            text: 'Успешно добавлено',
            type: 'success',
          });
        })
        .catch(function (error) {
          console.log('error');
          console.log(error);
        });
      },
      getEmploye() {
        //init employenik
        let dat = new Date();
        let str_dat = dat.getDate() + "-0" + (dat.getMonth()+1) + "-" + dat.getFullYear();
        if ((dat.getMonth()+1)>9){
          str_dat = dat.getDate() + "-" + (dat.getMonth()+1) + "-" + dat.getFullYear();
        }
        this.employe.fio = "";
        this.employe.birthday = str_dat;
        this.employe.phone = "";
        this.employe.sexy = 1;
        this.employe.sex = "муж.";
        this.employe.depart = "IT";
        document.title = `Сотрудник - новый`;
      }
  },
  created() {
    this.getEmploye();
  },
  watch: {
    '$route'() {
      this.getEmploye();
    }
  }
}
</script>
