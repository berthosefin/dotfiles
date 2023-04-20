import React from "react";
import TechList from "@/components/TechList";
import { json } from "stream/consumers";

const fetchTech = async (group: string) => {
  const res = await fetch(
    `http://127.0.0.1:8090/api/collections/tech/records?filter=(techGroupName="${group}")`
  );
  const response = await res.json();
  // return response;
  console.log(response);
};

type TypeProps = {
  params: {
    group: string;
  };
};

export default async function page({ params }: TypeProps) {
  const techlist = await fetchTech(params.group);
  console.log(techlist);
  // return <TechList techlist={techlist.items} group={params.group} />;
}
