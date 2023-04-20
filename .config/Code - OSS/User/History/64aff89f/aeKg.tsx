import React from "react";

const fetchTechGroup = async () => {
  const res = await fetch(
    "http://127.0.0.1:8090/api/collections/techGroup/records"
  );
  const { items } = await res.json();
  console.log(items);
  //   return data;
};

export default async function techGroup() {
  const techGroup = await fetchTechGroup();
  return <div>techGroup</div>;
}
