import axios from "axios"

export default {
    getFoods: () => {
        return axios.get('https://foodish-api.herokuapp.com/api/images/pizza')
    }
}