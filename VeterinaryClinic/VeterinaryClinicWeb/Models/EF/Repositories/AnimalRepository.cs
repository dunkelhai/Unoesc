using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class AnimalRepository : RepositoryBase<Animal>, IAnimalRepository
    {
        public AnimalRepository(BancoContext context) : base(context) { }

        protected override IQueryable<Animal> DefaultQuery =>
            base.DefaultQuery.Include(r => r.Responsible).Include(r => r.Race);
    }
}