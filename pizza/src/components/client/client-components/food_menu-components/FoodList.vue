<template>
    <div>
        <ul>
            <FoodListItem v-for="pizza in pizzas" v-bind:key="pizza" :food="pizza"></FoodListItem>
        </ul>
    </div>
</template>

<script>
import FoodListItem from './food_list-components/FoodListItem.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'FoodList',
    components: {
    FoodListItem,
    },
    props: ['pizza'],
    data() {
        return {
            pizzas: []
        }
    },
    methods: {
        ...mapActions(['fetchFood']),
    },
    computed: {
        ...mapGetters(['getFood']),
    },
    created() {
        this.fetchFood()
        this.pizzas = this.getFood
    }
}

</script>