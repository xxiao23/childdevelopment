<template>
  <div id="search">
    <input v-model="searchQuery" />
    <div v-for="r of resultQuery" :key="r.id">{{ r.area }} {{ r.tuition_rate }} {{ r.location }} {{ r.state }} {{ r.online_in_person }}</div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  setup() {
  },
  data() {
    return {
      searchQuery: null,
      resources: [
        { id: 1, area: "Coding", tuition_rate: "NA", location: "Hayward", state: "CA", online_in_person: "online" },
        { id: 2, area: "Math", tuition_rate: "$20/hour", location: "south bay", state: "CA", online_in_person: "online" }
      ]
    };
  },
  computed: {
    resultQuery() {
      if (this.searchQuery) {
        return this.resources.filter(item => {
          return this.searchQuery
            .toLowerCase()
            .split(" ")
            .every(v => item.area.toLowerCase().includes(v));
        });
      } else {
        return this.resources;
      }
    }
  }
};
</script>