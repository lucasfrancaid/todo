<template>
    <div class="hello">
        <h1> My first component using Vue.js, this is so cool. </h1>
        <p>
            <b>Message from Lucas:</b> {{ message }}
        </p>

        <div>
            <ol>
                <li v-for="task in tasks" :key="task.title">
                   <b> {{ task.title }} </b>
                </li>
            </ol>
        </div>

    </div>
</template>

<script>
import api from '../services/api';

export default {
    name: 'Tasks',
    props: {
        message: String
    },
    data: () => ({
        tasks: [
            { id: 1,title: 'Teste 1'},
            { id: 2,title: 'Teste 2'},
            { id: 3,title: 'Teste 3'},
        ]
    }),
    created() {
        api.get('api/task')
            .then((res) => {
                res.data.map(task => this.tasks.push(task))
            })
            .catch(err => console.log(err.data));
    }
};
</script>

<style scoped>
b {
    color: #42b983;
}
</style>