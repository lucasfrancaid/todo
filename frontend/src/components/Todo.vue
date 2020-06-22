<template>
    <v-container style="max-width: 500px; margin-top: 2.5em">
        <v-text-field
          v-model="task"
          label="What are you working on?"
          solo
          @keydown.enter="createTask"
        >
            <v-fade-transition v-slot:append>
                <v-icon
                    v-if="task"
                    @click="createTask"
                >
                    add_circle
                </v-icon>
            </v-fade-transition>
        </v-text-field>

        <h2 class="display-1 success--text pl-4">
            Tasks:&nbsp;
            <v-fade-transition leave-absolute>
                <span :key="`tasks-${tasks.length}`">
                    {{ tasks.length }}
                </span>
            </v-fade-transition>
        </h2>

        <v-divider class="mt-4"></v-divider>

        <v-row
          class="my-1"
          align="center"
        >
            <strong class="mx-4 info--text text--darken-2">
            Remaining: {{ remainingTasks }}
            </strong>

            <v-divider vertical></v-divider>

            <strong class="mx-4 success--text text--darken-2">
            Completed: {{ completedTasks }}
            </strong>

            <v-spacer></v-spacer>

            <v-progress-circular
            :value="progress"
            class="mr-2"
            ></v-progress-circular>
        </v-row>

        <v-divider class="mb-4"></v-divider>

            <v-card v-if="tasks.length > 0">
                <v-slide-y-transition
                class="py-0"
                group
                name="v-list"
                >
                    <template v-for="(task, i) in tasks">
                        <v-divider
                        v-if="i !== 0"
                        :key="`${i}-divider`"
                        ></v-divider>

                        <v-list-item :key="`${i}-${task.id}`">
                            <v-list-item-action>
                                <v-checkbox
                                @change="updateTask(task)"
                                v-model="task.done"
                                :color="task.done && 'grey' || 'primary'"
                                >
                                <template v-slot:label>
                                    <div
                                    :class="task.done && 'grey--text' || 'primary--text'"
                                    class="ml-4"
                                    v-text="task.title"
                                    ></div>
                                </template>
                                </v-checkbox>
                            </v-list-item-action>

                            <v-scroll-x-transition>
                                <v-icon
                                v-if="task.done"
                                color="success"
                                >
                                done
                                </v-icon>
                            </v-scroll-x-transition>

                            <v-spacer></v-spacer>

                            <v-icon
                            :key="`${task.id}-delete`"
                            @click="removeTask(task.id)"
                            >
                            delete
                            </v-icon>
                        </v-list-item>
                    </template>
                </v-slide-y-transition>
            </v-card>
        </v-container>
</template>

<script>
    import api from '../services/api';

    export default {

        data: () => ({
            tasks: [],
            task: null,
        }),
        created() {
            api.get('api/task')
                .then((res) => res.data.map(task => this.tasks.push(task)))
                .catch(err => console.log(err.data)
            );
        },

        computed: {
            completedTasks () {
                return this.tasks.filter(task => task.done).length
            },
            progress () {
                return this.completedTasks / this.tasks.length * 100
            },
            remainingTasks () {
                return this.tasks.length - this.completedTasks
            },
        },

        methods: {
            createTask () {
                const data = {
                    done: false,
                    title: this.task,
                    description: '',
                }

                api.post('api/task', data)
                    .then((res) => {
                        const data = res.data;
                        console.log('data post', data)
                        this.tasks.push({
                            id: data.id,
                            title: this.task,
                            description: data.description,
                        })
                        this.task = null
                    })
                    .catch(err => console.log(err.data)
                );
            },
            updateTask (task) {
                api.put(`api/task/${task.id}`, task)
                    .then((res) => {
                        const itemIndex = this.tasks.findIndex(element => element.id === res.data.id)
                        this.tasks[itemIndex] = task
                    })
                    .catch(err => console.log(err.data)
                );
            },
            removeTask (id) {
                api.delete(`api/task/${id}`)
                    .then((res) => {
                        console.log('Task was deleted', res.data)
                        const itemIndex = this.tasks.findIndex(element => element.id === id)
                        this.tasks.splice(itemIndex, 1)
                    })
                    .catch(err => console.log(err.data)
                );
            }
        },
    }  
</script>