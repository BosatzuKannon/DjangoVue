<template>
<h1>Lista de Categorías</h1>
    <ListDefault :elementsList="elements" />
</template>

<script>

import ListDefault from '../partials/_ListDefault'

export default {

    components:{
        ListDefault
    },

    created: function(){
        this.findAll()
    },

    data() {
        return {
            elements : []
        };
    },
    methods: {
        findAll: function(){
            
            fetch('http://127.0.0.1:8000/api/category/' + this.$route.params.id + '/elements/?format=json')
            .then(res => res.json() )
            .then(res => this.elements = res)
        },
        
    },
}
</script>

<style>

    .box{
        border: 1px solid #ccc;
        margin-bottom:5px;
    }
    
</style>