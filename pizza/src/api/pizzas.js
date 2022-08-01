import axios from "axios"
import base_url from "./base_url"

const url = base_url

export default {
    fetchAll: async (token) => {
        let response = await axios.get(url + 'api/pizzas/', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        })
        console.log(response.data)
        return response
    }
}