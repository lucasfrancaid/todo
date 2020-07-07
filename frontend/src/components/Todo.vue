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
			class="my-1"
			align="center"
		>

			<strong class="ml-16 mr-8 text--darken-2">
			TASKS:
			<v-fade-transition leave-absolute>
				<span :key="`tasks-${tasks.length}`">
					{{ tasks.length }}
				</span>
			</v-fade-transition>
			</strong>

			<v-divider vertical></v-divider>

			<strong class="mx-12 text--darken-2">
			TO DO: {{ remainingTasks }}
			</strong>

			<v-divider vertical></v-divider>

			<strong class="ml-10 mr-2 text--darken-2">
			DONE: {{ completedTasks }}
			</strong>

			<v-spacer></v-spacer>

			<v-progress-circular
			:value="progress"
			color="success"
			class="mr-4"
			></v-progress-circular>
		</v-row>

		<v-divider class="mb-5"></v-divider>

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
							:color="task.done && 'grey' || 'success'"
							>
							</v-checkbox>
						</v-list-item-action>
						<template v-if="!task.editing">
							<v-list-item-content>
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
							@blur="doneEdit($event, i)"
							@keyup.enter="doneEdit($event, i)"
							@keyup.esc="cancelEdit(i)"
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
							class="ml-4"
							>
							done
							</v-icon>
						</v-scroll-x-transition>

						<v-icon
						:key="`${task.id}-delete`"
						@click="removeTask(task.id)"
						class="ml-8"
						>
						delete
						</v-icon>
					</v-list-item>
				</template>
			</v-slide-y-transition>
		</v-card>

		<v-snackbar
			v-model="snackbar"
			:multi-line="true"
			:color="alertColor"
			>
			{{ text }}
			<template v-slot:action="{ attrs }">
				<v-btn
				color="white"
				text
				v-bind="attrs"
				@click="snackbar = false"
				>
				Close
				</v-btn>
			</template>
		</v-snackbar>
	
	</v-container>
</template>

<script>
	import api from '../services/api';

	export default {

		data: () => ({
			tasks: [],
			task: null,
			snackbar: false,
			text: 'Alert message',
			alertColor: 'success',
		}),
		created() {
			api.get('api/task')
				.then((res) => res.data.map(task => {
					task.editing = false
					this.tasks.push(task)
				}))
				.catch(err => {
					console.error(err.data)
					this.showAlert('Tasks could not loaded!', 'error')
				}
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
						this.showAlert('Task was created!')
					})
					.catch(err => {
						console.error(err.data)
						this.showAlert('Task could not created!', 'error')
					}
				);
			},
			updateTask (task) {
				api.put(`api/task/${task.id}`, task)
					.then((res) => {
						const itemIndex = this.tasks.findIndex(element => element.id === res.data.id)
						this.tasks[itemIndex] = task
						this.showAlert('Text was updated!')
					})
					.catch(err => {
						console.error(err.data)
						this.showAlert('Task could not updated!', 'error')
					}
				);
			},
			removeTask (id) {
				api.delete(`api/task/${id}`)
					.then(() => {
						const itemIndex = this.tasks.findIndex(element => element.id === id)
						this.tasks.splice(itemIndex, 1)
						this.showAlert('Task was deleted!')
					})
					.catch(err => {
						console.error(err.data)
						this.showAlert('Task could not deleted!', 'error')
					}
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
			showAlert (message='Success', type='success') {
				this.snackbar = true
				this.text = message
				this.alertColor = type
			}
		},
	}
</script>
