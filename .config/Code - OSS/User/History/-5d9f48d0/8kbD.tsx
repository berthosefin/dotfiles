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
    `http://127.0.0.1:8090/api/collections/tech/records?filter=id=${id}`
  );
  return res.json();
};

export default async function page({ params }: TypeProps) {
  const tech = await getTechDetails(params.tech);
  const techDetails = tech && tech.items ? tech.items[0] : {};
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 m-4">
      <div>
        <Image
          src={`http://127.0.0.1:8090/api/files/${techDetails.collectionId}/${techDetails.id}/${techDetails.image}`}
          width={500}
          height={500}
          alt="Tech Image"
          className="w-full"
        />
      </div>
      <div className="p-5">
        <h1>
          Tech Name:
          <span className="font-bold">{techDetails.name.toUpperCase()}</span>
        </h1>
        <div className="mt-3">
          <p>Tech Details: </p>
          <p className="bg-gray-200 p-4 rounded">{techDetails.description}</p>
        </div>
        <div className="mt-3">
          <p>Web Site: </p>
          <a
            target="_blank"
            rel="noreferrer"
            href={`https://www.${techDetails.name}.org`}
            className="text-[#81A1C1]"
          >
            https://www.{techDetails.name}.org
          </a>
        </div>
      </div>
    </div>
  );
}
