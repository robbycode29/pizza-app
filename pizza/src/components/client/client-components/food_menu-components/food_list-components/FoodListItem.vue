<template>
    <div>
        <li>
            <div class="bg-sky-200 w-full h-40 rounded-2xl flex flex-row hover:cursor-pointer hover:animate-pulse duration-75">
                <img :src="food.image" class="w-40 h-40 border-1 rounded-l-2xl border-sky-800"/>
                <div>
                    <h1 class="text-sky-800 font-bold text-xl pt-5">Make your own pizza!</h1>
                    <hr class="h-5 border-sky-200"/>
                    <p class="text-sky-800 font-bold text-lg p-5 pt-0">
                        Choose what ingredients go into your pizza. You have the best selection of ingredients available.
                    </p>
                </div>
            </div>
            <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                <ItemCustomization/>
            </transition>
        </li>
    </div>
</template>

<script>
import ItemCustomization from './food_list_item-components/ItemCustomization.vue';


export default {
    name: 'FoodListItem',
    props: ['food'],
    components: {
    ItemCustomization
    }
}

</script>