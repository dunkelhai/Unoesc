using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class ClinicRepository : RepositoryBase<Clinic>, IClinicRepository
    {
        public ClinicRepository(BancoContext context) : base(context) { }
    }
}