<template>
    <div>
        <li>
            <div class="bg-sky-200 w-full h-40 rounded-2xl flex flex-row hover:cursor-pointer hover:animate-pulse duration-75">
                <img :src="images[index].image" class="w-40 h-40 border-1 rounded-l-2xl border-sky-800"/>
                <div class="flex-grow">
                    <h1 class="text-sky-800 font-bold text-xl pt-5">{{food.name}}</h1>
                    <hr class="h-5 border-sky-200"/>
                    <p class="text-sky-800 font-bold text-lg p-5 pt-0">
                        This pizza contains the following ingredients: 
                        <ul class="flex flex-row gap-5 justify-center">
                            <p class="text-emerald-700" v-for="ingredient in food.ingredients" :key="ingredient.id">{{ingredient.name}} </p>
                        </ul>
                        
                    </p>
                </div>
            </div>
            <ItemCustomization class="invisible"/>
        </li>
    </div>
</template>

<script>
import ItemCustomization from './food_list_item-components/ItemCustomization.vue';

export default {
    name: 'FoodListItem',
    props: ['food', 'images', 'index'],
    components: {
    ItemCustomization,
}
}

</script>