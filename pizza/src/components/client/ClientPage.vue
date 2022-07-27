<template>
    <div class="h-screen">
        <NavBar/>
        <div class="bg-sky-800 h-full w-full flex justify-center">
            <router-view class="bg-teal-100 w-11/12 h-fit rounded-b-3xl"/>
        </div>
    </div>
</template>

<script>
    import NavBar from './NavBar.vue'

    export default {
        name: 'ClientPage',
        components: {
            NavBar,
        }
    }
</script>