<template>
    <div class="w-screen h-screen flex justify-center items-center bg-sky-700">
        <div class="bg-emerald-200 w-3/4 h-3/5 flex flex-col justify-center items-center rounded-3xl " width="50rem">
            <h1 class="text-sky-900 font-bold text-2xl">Welcome to Pizza App</h1>
            <hr class="h-10"/>
            <div class="flex flex-col gap-5">
                <router-link to="/client/food-menu" class="bg-emerald-50 font-semibold p-1 px-7 rounded-3xl border-sky-700 border-2 hover:bg-sky-700 duration-200 hover:text-white cursor-pointer">Client</router-link>
                <router-link to="/admin" class="bg-emerald-50 font-semibold p-1 px-7 rounded-3xl border-sky-700 border-2 hover:bg-sky-700 duration-200 hover:text-white cursor-pointer">Admin</router-link>
            </div> 
        </div>
    </div>
</template>

<script>

export default {
  name: 'LoginPage',
}


</script>

<style>
    
</style>