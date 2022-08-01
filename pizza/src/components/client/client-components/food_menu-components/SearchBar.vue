<template>
    <div>
        <h1 class="text-sky-800 font-semibold self-start">Search for pizza:</h1>
        <input @input="search()" v-model="searchQuery" class="w-full border-2 border-sky-800 rounded-lg"/>
    </div>
</template>

<script>

import { mapMutations, mapGetters, mapActions } from 'vuex'

export default {
    name: 'SearchBar',
    data() {
        return {
            searchQuery: '',
            searchResult: [],
        }
    },
    computed: {
        ...mapMutations(['setPizzas']),
        ...mapMutations(['restorePizzasBackup']),
        ...mapGetters(['getPizzasBackup']),
        ...mapGetters(['getPizzas']),
    },
    methods: {
        ...mapActions(['modifyPizzas']),
        search() {
            this.searchResult = []
            Object.keys(this.getPizzasBackup).forEach(key => {
                if (this.getPizzasBackup[key].name.toLowerCase().includes(this.searchQuery.toLowerCase())) {
                    this.searchResult.push(this.getPizzasBackup[key])
                }
            })
            this.modifyPizzas(this.searchResult)
            if (this.searchQuery == '') {
                this.restorePizzasBackup()
            }
        }
    }

}

</script>