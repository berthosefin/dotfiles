"use client";

import Image from "next/image";

const Avatar = () => {
  return (
    <div>
      <Image
        className="rounded-full"
        height="30"
        width="30"
        alt="Avater"
        src="/images/placeholder.jpg"
      />
    </div>
  );
};

export default Avatar;
