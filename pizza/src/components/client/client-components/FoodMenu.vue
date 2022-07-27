<template>
    <div class="flex flex-col items-center gap-10">
       <SearchBar class="mt-12 w-1/2 flex flex-col items-center"/>
       <hr class="border-sky-800 w-3/4 border-1 rounded-full"/>
       <CustomPizzaGenerator class="w-1/2 flex flex-col items-center"/>
       <FoodList/>
    </div>
</template>

<script>
import SearchBar from './food_menu-components/SearchBar.vue'
import CustomPizzaGenerator from './food_menu-components/CustomPizzaGenerator.vue'
import FoodList from './food_menu-components/FoodList.vue'

export default {
    name: 'FoodMenu',
    components: {
    SearchBar,
    CustomPizzaGenerator,
    FoodList
}
}
</script>