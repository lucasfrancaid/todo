<template>
	<v-container style="max-width: 500px; margin-top: 1em">
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

		<v-divider class="mt-0"></v-divider>

		<v-row
			class="my-1 divider"
			align="center"
		>

			<strong class="divider-item text--darken-2">
			TASKS:
			<v-fade-transition leave-absolute>
				<span :key="`tasks-${tasks.length}`">
					{{ tasks.length }}
				</span>
			</v-fade-transition>
			</strong>

			<v-divider vertical></v-divider>

			<strong class="divider-item text--darken-2">
			TO DO: {{ remainingTasks }}
			</strong>

			<v-divider vertical></v-divider>

			<strong class="divider-item text--darken-2">
			DONE: {{ completedTasks }}
			</strong>

		</v-row>

		<v-progress-linear
			:value="progress"
			color="success"
			class=""
		></v-progress-linear>

		<v-divider class="mb-5"></v-divider>

		<template v-if="tasks.length > 0">
			<draggable v-model="tasks">
				<transition-group>
					<v-card v-for="(task, index) in tasks" :key="index">
						<v-divider
						v-if="index !== 0"
						:key="`${index}-divider`"
						></v-divider>

						<v-list-item :key="`${index}-${task.id}`">
							<v-list-item-action class="mr-3">
								<v-checkbox
								@change="updateTask(task)"
								v-model="task.done"
								:color="task.done && 'grey' || 'success'"
								>
								</v-checkbox>
							</v-list-item-action>
							<template v-if="!task.editing">
								<v-list-item-content class="mr-2">
									<div
									:class="task.done && 'grey--text' || 'success--text'"
									class="ml-4"
									v-text="task.title"
									@click="task.editing = true"
									></div>
								</v-list-item-content>
							</template>
							<v-text-field
								:value="task.title"
								@blur="doneEdit($event, index)"
								@keyup.enter="doneEdit($event, index)"
								@keyup.esc="cancelEdit(index)"
								class="ml-1"
								color="primary"
								autofocus
								hide-details
								flat
								solo
								v-else
							></v-text-field>

							<v-scroll-x-transition>
								<v-icon
								v-if="task.done"
								color="success"
								>
								done
								</v-icon>
							</v-scroll-x-transition>

							<v-icon
							:key="`${task.id}-delete`"
							@click="removeTask(task.id)"
							class="ml-5"
							>
							delete
							</v-icon>
						</v-list-item>
					</v-card>
				</transition-group>
			</draggable>
		</template>
	</v-container>
</template>

<script>
	import api from '../services/api';
	import draggable from 'vuedraggable';

	export default {

		components: {
			draggable,
		},
		data: () => ({
			tasks: [],
			task: null,
		}),
		created() {
			api.get('api/task')
				.then((res) => res.data.map(task => {
					task.editing = false
					this.tasks.push(task)
				}))
				.catch(err => console.error(err.data)
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
				const task = {
					done: false,
					title: this.task,
					description: '',
					editing: false,
				};

				api.post('api/task', task)
					.then((res) => {
						const data = res.data;
						this.tasks.push({
							id: data.id,
							title: this.task,
							description: data.description,
							editing: false,
						})
						this.task = null
					})
					.catch(err => console.error(err.data)
				);
			},
			updateTask (task) {
				api.put(`api/task/${task.id}`, task)
					.then((res) => {
						const itemIndex = this.tasks.findIndex(element => element.id === res.data.id)
						this.tasks[itemIndex] = task
					})
					.catch(err => console.error(err.data)
				);
			},
			removeTask (id) {
				api.delete(`api/task/${id}`)
					.then(() => {
						const itemIndex = this.tasks.findIndex(element => element.id === id)
						this.tasks.splice(itemIndex, 1)
					})
					.catch(err => console.error(err.data)
				);
			},
			doneEdit (event, index) {
				const title = event.target.value
				if (title !== this.tasks[index].title) {
					let task = this.tasks[index]
					task.title = title
					task.editing = false
					this.updateTask(task)
				} else {
					this.tasks[index].editing = false
				}
			},
			cancelEdit (index) {
				this.tasks[index].editing = false
			},
		},
	}
</script>

<style scoped>
.divider {
	justify-content: center;
}
.divider-item {
	margin: 0 7%
}
.v-sheet.v-card {
    border-radius: 0;
}
</style>