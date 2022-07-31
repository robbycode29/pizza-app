<template>
    <div class="w-screen h-screen flex justify-center items-center bg-sky-700">
        <div class="bg-emerald-200 w-3/4 h-3/5 flex flex-col justify-center items-center rounded-3xl " width="50rem">
            <!-- <h1 class="text-sky-900 font-bold text-2xl">Welcome to Pizza App</h1>
            <hr class="h-10"/>
            <div class="flex flex-col gap-5">
                <router-link to="/client/food-menu" class="bg-emerald-50 font-semibold p-1 px-7 rounded-3xl border-sky-700 border-2 hover:bg-sky-700 duration-200 hover:text-white cursor-pointer">Client</router-link>
                <router-link to="/admin" class="bg-emerald-50 font-semibold p-1 px-7 rounded-3xl border-sky-700 border-2 hover:bg-sky-700 duration-200 hover:text-white cursor-pointer">Admin</router-link>
            </div>  -->
            <form>
                <div class="flex flex-col gap-5">
                    <label class="text-sky-900 font-bold text-2xl" for="email">Username</label>
                    <input v-model="username" class="bg-sky-100 border-sky-700 border-2 p-1 px-7 rounded-3xl" type="username" name="username" id="username" placeholder="Enter your username" />
                </div>
                <hr class="mb-7 border-emerald-200"/>
                <div class="flex flex-col gap-5">
                    <label class="text-sky-900 font-bold text-2xl" for="password">Password</label>
                    <input v-model="password" class="bg-sky-100 border-sky-700 border-2 p-1 px-7 rounded-3xl" type="password" name="password" id="password" placeholder="Enter your password" />
                </div>
                <hr class="m-7 border-emerald-200"/>
                <div class="flex flex-col gap-5">
                    <button @click.prevent="$emit('close')" type="submit" @click="onClick()" class="bg-emerald-50 font-semibold p-1 px-7 rounded-3xl border-sky-700 border-2 hover:bg-sky-700 duration-200 hover:text-white cursor-pointer">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
            access: '',
            refresh: '',
        }
    },

    methods: {
        onClick() {
            this.login({
                username: this.username,
                password: this.password
            }).then(() => {
                this.access = this.getAccess
                this.refresh = this.getRefresh
                
                if (this.access) {
                    this.$router.push('/client/food-menu')
                } 
                else {
                    console.log('try again!')
                }
            })
        },
        ...mapActions(['login']),
    },

    computed: {
        ...mapGetters(['getAccess']),
        ...mapGetters(['getRefresh']),
    },
}


</script>

<style>
    
</style>