type PageProps = {
  params: {
    searchTerm: string;
  };
};

const search = async (searchTerm: string) => {
  const res = await fetch(`http://127.0.0.1:3001/`);
};

export default async function SearchResults({
  params: { searchTerm },
}: PageProps) {
  const SearchResults = await search(searchTerm);
  return <div>SearchResults</div>;
}
