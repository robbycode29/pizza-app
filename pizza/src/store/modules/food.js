import api from "../../api/foodish-api"

const state = {
    food: [],
}

const getters = {
    getFood: state => state.food,
}

const actions = {    
    async fetchFood({ commit }) {
        let pizzas = []
        for (let i = 0; i < 10; i++) {
            let response = await api.getFoods();
            pizzas.push(response.data);
        }
        // let response = await api.getFoods();
        // console.log(response.data.image);
        commit("setFood", pizzas);
    }
}

const mutations = {
    setFood: (state, food) => {
        state.food = food
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}