<template>
    <div>
        <div class="bg-sky-200 w-full h-40 rounded-2xl flex flex-row hover:cursor-pointer hover:animate-pulse">
            <img src="../../../../assets/pizza.png" class="w-40 h-40 border-1 rounded-l-2xl border-sky-800"/>
            <div>
                
                <h1 class="text-sky-800 font-bold text-xl pt-5">Make your own pizza!</h1>
                <hr class="h-5 border-sky-200"/>
                <p class="text-sky-800 font-bold text-lg p-5 pt-0">
                    Choose what ingredients go into your pizza. You have the best selection of ingredients available.
                </p>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'CustomPizzaGenerator',
    components: {

    }
}

</script>