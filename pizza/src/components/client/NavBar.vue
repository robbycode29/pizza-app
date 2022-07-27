<template>
    <div class="bg-emerald-500 w-screen h-12 flex items-center flex-row">
        <a href="/client/food-menu" class="ml-7 text-emerald-50 font-semibold hover:cursor-pointer hover:text-lg duration-200">Pizza App</a>
        <div class="flex-1"></div>
        <div>
            <router-link to="/client/food-menu"  class="mr-7 text-emerald-50 font-semibold hover:cursor-pointer hover:text-lg duration-200">Pizza Menu</router-link>
            <router-link to="/client/order-history" class="mr-7 text-emerald-50 font-semibold hover:cursor-pointer hover:text-lg duration-200">Order History</router-link>
            <router-link to="/client/shopping-cart" class="mr-7 text-emerald-50 font-semibold hover:cursor-pointer hover:text-lg duration-200">Cart</router-link>
            <router-link to="/" class="mr-7 text-emerald-50 font-semibold hover:cursor-pointer hover:text-lg duration-200">Logout</router-link>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'NavBar',
        components: {
        }
    }
</script>