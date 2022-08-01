<template>
    <div>
        <ul>
            <FoodListItem v-for="pizza in pizzas" v-bind:key="pizza" :food="pizza" :images="images" :index="pizza.id"></FoodListItem>
        </ul>
    </div>
</template>

<script>
import FoodListItem from './food_list-components/FoodListItem.vue'

import { mapActions, mapGetters, mapState } from 'vuex'

export default {
    name: 'FoodList',
    components: {
    FoodListItem,
    },
    data() {
        return {
            pizzas: this.pizzas,
            images: [],
        }
    },
    methods: {
        ...mapActions(['fetchPizzas', 'fetchFood']),
    },
    computed: {
        ...mapGetters(['getPizzas', 'getFood']),
        ...mapState(['pizzas']),
    },
    created() {
        this.fetchPizzas()
        this.fetchFood()
        this.images = this.getFood
        this.pizzas = this.getPizzas
    }
}

</script>