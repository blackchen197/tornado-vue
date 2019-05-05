<template>
  <div class="col-md-12">
    <button @click="add" class="btn btn-primary btn-sm" style="margin:10px 0 10px 0">Добавить</button>
    <b-table striped hover :items="all" :fields="fields" class="col-md-6 employee">
      <template slot="actions" slot-scope="row">
        <b-button size="sm" variant="info" @click="salary(row.item, row.index, $event.target)" class="mr-2">
         Зарплата
        </b-button>
      </template>
      <template slot="fio" slot-scope="data">
      <b-link :to="{ name: 'employee', params: { id: data.value.id }}">
        {{data.value.fio}}
      </b-link>
    </template>
    </b-table>
        <b-modal id="modalSalary" ref="modalSalary" :title="modalSalary.title" ok-only @ok="handleButton">
          <form @submit="handleSubmit">
            <b-form-input type="text"
                      placeholder="Сумма"
                      v-model="summ" value="0"></b-form-input>
                      <p v-if="errors.length">
                          <span v-for="error in errors">{{ error }}</span>
                      </p>
            </form>
        </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  title: `Учёт персонала`,
  data () {
      return {
        fields: [
        {
          key: 'id',
          label: 'id',
          sortable: false
        },
        {
          key: 'fio',
          label: 'Фамилия И.О.',
          sortable: true
        },
        {
          key: 'birthday',
          label: 'Дата рождения',
          sortable: true
        },
        {
          key: 'sex',
          label: 'Пол',
          sortable: true,
          formatter: (value) => { if (value == 0){ return "муж." }else{ return "жен." } }
        },
        {
          key: 'depart',
          label: 'Отдел',
          sortable: true
        },
        {
          key: 'phone',
          label: 'Телефон',
          sortable: true
        },
        {
          key: 'actions',
          label: 'Действия',
          sortable: false
        },
      ],
      errors: [],
      modalSalary: { title: '', content: '', id: 0 },
      all: [],
      summ:0,
      employee:0,
      endpoint: 'http://localhost:5000/api/all',
      }
    },
    created() {
      this.getAll();
    },
    methods: {
            getAll() {
              axios.get(this.endpoint)
                .then(response => {
                  this.all = response.data;
                })
                .catch(error => {
                  console.log('error');
                  console.log(error);
                })
            },
            add () {
              this.$router.push({path: '/add' });
            },
            handleButton (evt) {
              this.errors = [];
              evt.preventDefault();
              if (this.summ == 0 || this.summ.match(/^-?\d*(\.\d+)?$/) == null || this.summ < 0) {
                this.errors.push('Введите корректную сумму.');
                return false;
                }
              else {
                this.handleSubmit();
                }
            },
            handleSubmit () {
              const path = 'http://localhost:5000/api/salary';
              var vm = this
              axios.post(path,
                {
                    employee:  vm.employee,
                    summ:  vm.summ
                }
              )
                .then(function (response) {
                  vm.$refs.modalSalary.hide();
                  vm.summ = 0;
                  vm.$notify({
                    group: 'foo',
                    text: 'Успешно сохранено',
                    type: 'success',
                  });
                })
                .catch(function (error) {
                  console.log('error');
                  console.log(error);
                });
            },
            salary (item, index, button) {
              console.log(item.fio)
              this.modalSalary.title = `Зарплата для: ${item.fio.fio}`;
              this.modalSalary.id = item.id;
              this.employee = item.id;
              this.$root.$emit('bv::show::modal', 'modalSalary', button);
            },
          },
}

</script>

<style>

</style>
