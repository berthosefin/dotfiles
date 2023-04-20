import React from "react";

const fetchTechGroup = async () => {
  const res = await fetch(
    "http://127.0.0.1:8090/api/collections/techGroup/records"
  );
  const data = await res.json();
  console.log(data.items.map((item: string) => item.name));
  //   return data;
};

export default async function techGroup() {
  const techGroup = await fetchTechGroup();
  return <div>techGroup</div>;
}
