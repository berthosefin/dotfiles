import React from "react";
import Image from "next/image";

type TypeProps = {
  params: {
    group: string;
    tech: string;
  };
};

const getTechDetails = async (id: string) => {
  const res = await fetch(
    `http://127.0.0.1:8090/api/collections/tech/records?filter=(id="${id}")`
  );
  return res.json();
};

export default async function page({ params }: TypeProps) {
  const tech = await getTechDetails(params.tech);
  const techDetails = tech.items[0];
  return (
    <div className="grid grid-cols-1 md:grid-cols-2">
      <div className="">
        <Image
          src={`http://127.0.0.1:8090/api/files/${techDetails.collectionId}/${techDetails.id}/${techDetails.image}`}
          width={500}
          height={500}
          alt="Tech Image"
          className="w-full"
        />
      </div>
      <div>
        <h1>
          Tech Name: <span>{techDetails.name}</span>
        </h1>
      </div>
    </div>
  );
}
