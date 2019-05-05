<template>
  <div class="col-md-12">
    <h3>Зарплаты</h3>
    <b-link :to="{ name: 'employee',params: { id: this.id }}">
      Назад
    </b-link>
    <b-table hover :items="all" :fields="fields" class="col-md-6">
    </b-table>
  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    props: ['id'],
    title: `Зарплаты`,
    data(){
    return {
    all: [],
    fields: [
      {
        key: 'date',
        label: 'Дата выплаты',
        sortable: true
      },
    {
      key: 'fio',
      label: 'Фамилия И.О.',
      sortable: false
    },

    {
      key: 'summ',
      label: 'Сумма',
      sortable: true
    }

  ],}
    },
    methods: {
      getSalary(id) {
        const path = 'http://localhost:5000/api/salary/' + id
        axios(path)
          .then(response => {
            this.all = response.data;
          })
          .catch( error => {
            console.log('error');
            console.log(error)
          })
      }
    },
    created() {
      this.getSalary(this.id);
    },
    watch: {
      '$route'() {
        this.getSalary(this.id);
      }
    }
  }
</script>
