using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class SpecieRepository : RepositoryBase<Specie>, ISpecieRepository
    {
        public SpecieRepository(BancoContext context) : base(context) { }
    }
}